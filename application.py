import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash
from time import gmtime, strftime

from helpers import apology, login_required, lookup, usd

#ADDED password() to change password
#ADDED addcash() to top up cash

# Ensure environment variable is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    #Get user's cash holdings
    cash = db.execute("SELECT cash FROM users WHERE id = :id", id = session["user_id"])

    #Store cash total in grandtotal variable
    grandtotal = cash[0]["cash"]

    #Get users' unique stock holdings (Symbol and Shares)
    stocks = db.execute("SELECT Symbol, SUM(Shares) AS Total_Shares FROM history WHERE user=:user_id GROUP BY Symbol", user_id=session["user_id"])

    #For every stock in list, store symbol, number of shares, price and total
    for stock in stocks:
        symbol = stock["Symbol"]
        shares = int(stock["Total_Shares"])
        price = ""
        total = ""

        a = lookup(symbol)

        #Get current price of stock from lookup function and store.
        stock["price"] = "{:.2f}".format(a["price"])
        stock["total"] = "{:.2f}".format(a["price"] * shares)
        stock["grandtotal"] = (a["price"]) * shares

        #Add on each stock's total value to grand total
        grandtotal += stock["grandtotal"]

    grandtotal = "{:.2f}".format(grandtotal)

    return render_template("index.html", stocks = stocks, cash = cash, grandtotal = grandtotal)

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    if request.method == "POST":
        buy = lookup(request.form.get("symbol"))

        if not buy:
            return apology("Invalid symbol")

        #check for valid whole numbers
        if not request.form.get("shares").isdigit():
            return apology("Invalid shares")

        shares = int(request.form.get("shares"))

        if shares <= 0:
            return apology("Invalid number of shares")

        #select user's cash holdings from db
        funds = db.execute("SELECT cash FROM users WHERE id=:user_id;", user_id=session["user_id"])
        funds = funds[0]['cash']

        p = round(float(buy["price"]),2)

        if funds < shares * round(float(shares * p),2):

            return apology("Not enough Cash")


        db.execute("INSERT INTO history (Symbol, Shares, Price, User, DateTime, Type) VALUES (:symbol, :shares, :price, :id, :Date, :Type)", symbol = buy["symbol"], shares = shares,
                        price = p, id=session["user_id"], Date = strftime("%Y-%m-%d %H:%M:%S", gmtime()), Type = 'B')


        db.execute("UPDATE users SET cash = cash - :total WHERE id=:user_id;", total = (p * shares), user_id = session["user_id"])

        return redirect("/")

    else:

        return render_template("buy.html")

@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    histories  = db.execute("SELECT * from history WHERE user=:id", id=session["user_id"])

    return render_template("history.html", histories = histories)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    if request.method == "POST":
        quote = lookup(request.form.get("symbol"))

        if not quote:
            return apology("Missing symbol")

        if quote == None:
            return apology("Invalid symbol")

        return render_template("quoted.html", symbol = quote["symbol"], price = usd(quote["price"]))

    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "POST":

        #Ensure user input a username, else apology
        if not request.form.get("username"):
            return apology("Username cannot be blank")

        #Ensure password input, else apology
        if not request.form.get("password"):
            return apology("Password cannot be blank")

        #Ensure confirmation input else apology, ensure confirmation same as password, else apology
        if not request.form.get("confirmation"):
            return apology("Confirmation cannot be blank")

        if request.form.get("password") != request.form.get("confirmation"):
            return apology("Password and Confirmation does not match")

        #Hash password
        password = request.form.get("password")
        hash = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)

        #Store Username and Hash of password
        result = db.execute("INSERT INTO users (username, hash) VALUES (:username, :hash)", username=request.form.get("username"), hash=hash)

        #check for existing username
        if not result:
            return apology("Username exists")

        #Store session id in session
        session["user_id"] = result

        return redirect("login")

    else:
        return render_template("register.html")

@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    if request.method == "POST":

        symbol = lookup(request.form.get("symbol"))

        if not symbol:
            return apology("Invalid Symbol")

        a = request.form.get("shares")

        if not a:
            return apology("Invalid Number of Shares")

        shares = int(request.form.get("shares"))

        if shares <=0:
            return apology("Invalid Shares Quantity")

        #Select shares that user owns from db
        own = db.execute("SELECT Symbol, SUM(Shares) FROM history WHERE User = :id AND Symbol=:symbol GROUP BY Symbol", id = session["user_id"], symbol = symbol["symbol"])

        #check for adequate shares to sell
        if not own:
            return apology("You do not own these shares")

        if shares > own[0]['SUM(Shares)']:
            return apology("you don't own that many stocks")

        #Update sell in history
        db.execute("INSERT INTO history (Symbol, Shares, User, Price, DateTime, Type) VALUES(:symbol, :shares, :id, :price, :DateTime, :Type)", symbol = symbol["symbol"], shares = -shares, price=usd(symbol["price"]), id = session["user_id"], DateTime = strftime("%Y-%m-%d %H:%M:%S", gmtime()), Type = 'S')

        price = round(float(symbol["price"]),2)
        cost = round(float(shares * price),2)

        #Update user cash holdings, adding cost of sale to cash holdings
        db.execute("UPDATE users SET cash = cash + :cost WHERE id = :user_id;", cost = cost , user_id = session["user_id"])


        return redirect("/")

    else:
        return render_template("sell.html")

@app.route("/password", methods=["GET", "POST"])
@login_required
#Newly added function
def password():

    if request.method == "POST":

        #Ensure password input, else apology
        if not request.form.get("newpassword"):
            return apology("New Password cannot be blank")

        #Ensure confirmation input else apology, ensure confirmation same as password, else apology
        if not request.form.get("newpasswordconfirm"):
            return apology("Please enter new password confirmation")

        if request.form.get("newpassword") != request.form.get("newpasswordconfirm"):
            return apology("New Password and Confirmation does not match")

        #Hash password
        newpassword = request.form.get("newpassword")
        hash = generate_password_hash(newpassword, method='pbkdf2:sha256', salt_length=8)

        #Store Username and Hash of password
        db.execute("UPDATE users SET hash = :hash WHERE id=:id", id=session["user_id"], hash=hash)

        return redirect("/")


    else:
        return render_template("password.html")

@app.route("/addcash", methods=["GET", "POST"])
@login_required
#Newly added function
def addcash():

    #Extract cash holdings of user from db. Also to show current cash holding in html page.
    funds = db.execute("SELECT cash FROM users WHERE id=:user_id;", user_id=session["user_id"])

    if request.method == "POST":

        #Ensure amount is not blank
        if not request.form.get("addcash"):
            return apology("Cash amount cannot be blank")

        #Update cash holdings
        a = float(funds[0]["cash"])
        b = int(request.form.get("addcash"))
        db.execute("UPDATE users SET cash = :cash WHERE id=:id", id=session["user_id"], cash = a + b)

        return redirect("/")


    else:
        return render_template("addcash.html", funds = funds)



def errorhandler(e):
    """Handle error"""
    return apology(e.name, e.code)


# listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)




