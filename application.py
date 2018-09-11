from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
import datetime
from time import gmtime, strftime
import time
import urllib.request
import json
# import library from https://github.com/mtusman/gemini-python
import gemini
#To enable threading
import threading


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

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

#provide public and private API keys for websocket connection
r = gemini.PrivateClient("Vk5HgHCe3RD3RQLI4ngj", "4HiK4Hc4HKsdSWc7LpJd47LqGxYF", sandbox=True)

#Sandbox url. Change to live url for live envt
base_url = "https://api.sandbox.gemini.com/v1"

#Function to get latest price from exchange & compare to stop loss positions in db. Comparison is combined in this function due to rate limiting of API.
#Return price for display in index page
def btc_price():

    #Get BTC Price and parse json
    response = urllib.request.urlopen(base_url + "/pubticker/btcusd")
    a = (response.read())
    b = json.loads(a)

    #return latest BTC price
    p = b["last"]

    return(p)

#Single homepage that display balances, histories, open orders
@app.route("/", methods=["GET", "POST"])
def index():
    """Home Page - Show Balances, Trade History, Price and Open Orders"""

    #Get BTC price
    p_btc = btc_price()

    #Timestamp to show time of last refresh
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    #Get Balances data from exchange. Gemini returns a list of dict
    balance = r.get_balance()
    balance_BTC = balance[0]["amount"]
    balanceBTC_available = balance[0]["available"]
    balance_USD = balance[1]["amount"]
    balanceUSD_available = balance[1]["available"]

    #Get Trade History from exchange using API client
    past_trade_data = r.get_past_trades("BTCUSD")

    #Loop through array of dict for trade history data returned by API
    for i in range(0, len(past_trade_data)):

        #delete unneeded dict keys
        del past_trade_data[i]['aggressor']
        del past_trade_data[i]['timestampms']
        del past_trade_data[i]['fee_currency']
        del past_trade_data[i]['tid']
        del past_trade_data[i]['exchange']
        del past_trade_data[i]['is_auction_fill']
        del past_trade_data[i]['fee_amount']

        #convert timestamp from epoch to human readable
        past_trade_data[i]['timestamp'] = datetime.datetime.fromtimestamp(past_trade_data[i]['timestamp']).strftime('%d/%b/%y, %H:%M')

        #rename dict keys
        past_trade_data[i]['Order Id'] = past_trade_data[i].pop('order_id')
        past_trade_data[i]['Buy/Sell'] = past_trade_data[i].pop('type')
        past_trade_data[i]['Price Bought'] = past_trade_data[i].pop('price')
        past_trade_data[i]['BTC Amount'] = past_trade_data[i].pop('amount')
        past_trade_data[i]['Date/Time'] = past_trade_data[i].pop('timestamp')

    #Limit to last 10 data for aesthetics
    past_trade_data = past_trade_data[:10]

    #Get Open Orders from exchange
    active_order = r.active_orders()

    #Loop through array of dict for open orders submitted to exchange. Data returned from API
    for i in range(0, len(active_order)):

        #delete unneeded dict keys
        del active_order[i]['symbol']
        del active_order[i]['id']
        del active_order[i]['exchange']
        del active_order[i]['avg_execution_price']
        del active_order[i]['type']
        del active_order[i]['timestampms']
        del active_order[i]['is_live']
        del active_order[i]['is_cancelled']
        del active_order[i]['is_hidden']
        del active_order[i]['was_forced']
        del active_order[i]['options']
        del active_order[i]['remaining_amount']

        #convert timestamp from epoch to human readable
        active_order[i]['timestamp'] = datetime.datetime.fromtimestamp(int(active_order[i]['timestamp'])).strftime('%d/%b/%y, %H:%M')

        #rename dict keys
        active_order[i]['Order Id'] = active_order[i].pop('order_id')
        active_order[i]['Buy/Sell'] = active_order[i].pop('side')
        active_order[i]['Price'] = active_order[i].pop('price')
        active_order[i]['Executed Amount'] = active_order[i].pop('executed_amount')
        active_order[i]['Original Amount'] = active_order[i].pop('original_amount')
        active_order[i]['Date/Time'] = active_order[i].pop('timestamp')


    #Get Stop Losses records from db
    stop = db.execute("SELECT No, price, amount FROM stops")

    #Handle Cancel Orders
    if request.method == "POST":


        cancel = request.form.get("order_id")
        sl = request.form.get("No")

        if not cancel:
            pass
        else:
            #Cancel Open Buy and Sell limits sent to Exchange
            r.cancel_order(cancel)


        if not sl:
            pass
        else:
            #Cancel pending stop losses stored in db
            db.execute("DELETE FROM stops WHERE No = :b ", b=sl)


        #Refresh homepage to reflect changes
        return redirect("/")


    return render_template("index.html", now=now, p_btc=p_btc, balance_BTC=balance_BTC,
    balanceBTC_available=balanceBTC_available,
    balance_USD=balance_USD, balanceUSD_available=balanceUSD_available,
    past_trade_data = past_trade_data, active_order=active_order, stop=stop)


#Trade function for buying and selling orders
@app.route("/trade", methods=["GET", "POST"])
def trade():

    error = ''
    good_buy = ''
    good_sell = ''
    good_stop = ''

    if request.method == "POST":

        #trade input in jinja is a radio selection. Hence, no need to test for null input.
        if request.form.get("trade") =="Buy":

            #Check for valid amount
            try:
                float(request.form.get("amount"))

            #if error to show error flash message
            except ValueError:
                error = 'Invalid amount'

            buy_amt = request.form.get("amount")


            #Check for valid price
            try:
                float(request.form.get("price"))

            #if error to show error flash message
            except ValueError:
                error = 'Invalid price'

            buy_price = request.form.get("price")

            #option empty array specifies a limit order according to API doc
            r.new_order("BTCUSD", buy_amt, buy_price, "buy", options=[])
            good_buy = 'Buy Order Submitted'

        if request.form.get("trade") =="Sell":

            #Check for valid amount
            try:
                float(request.form.get("amount"))

            #if error to show error flash message
            except ValueError:
                error = 'Invalid amount'

            sell_amt = request.form.get("amount")

            try:
                float(request.form.get("price"))

            #if error to show error flash message
            except ValueError:
                error = 'Invalid price'

            sell_price = request.form.get("price")

            latest_price = btc_price()

            #Compares sell price of order from user to latest price
            if float(sell_price) < float(latest_price):

                #keep sell order in database as a stop loss
                db.execute("INSERT INTO stops (price, amount) VALUES (:price, :amount)", price = sell_price, amount = sell_amt)

                good_stop = 'Stop Loss Order Submitted'

            #Execute sell order and send to exchange
            else:
                r.new_order("BTCUSD", sell_amt, sell_price, "sell", options=[])
                good_sell = 'Sell Order Submitted'

    return render_template("trade.html", error = error, good_buy = good_buy, good_stop = good_stop, good_sell = good_sell)


#Stop loss function that runs every 2s perpetually. Extracts stop loss records from db and compares to latest price from API.
def stop_loss():
    threading.Timer(2.0, stop_loss).start() # called every 2s perpetually

    #Stores array of dict of stop loss records in var
    stop = db.execute("SELECT * FROM stops")

    #Call latest price function to get latest price from API
    btcp = btc_price()

    #Loop through each array record and compare price
    for i in range(0, len(stop)):
        b= (stop[i]['Price'])

        #If stop loss price hits latest price, to execute sell order to submit to exchange, delete record from db
        if float(b) >= float(btcp):

            r.new_order("BTCUSD", str(stop[i]['Amount']) , str(stop[i]['Price']), "sell", options=[])

            db.execute("DELETE FROM stops WHERE No = :a ", a=stop[i]['No'])

stop_loss()




