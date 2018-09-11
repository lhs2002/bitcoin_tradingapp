# Design Document for Gemini Trading App

## Technical Objective
Connect to Gemini API, request for price, balances, trade history, open orders and format it for presentation. Submit buy/sell orders to Gemini. Implement stop loss feature.

## App Structure
Backend python serves as the engine that runs the app and supported by sql db. Html files provide the frontend webpages that interacts with user inputs.

## Specification

### application.py
The only python file used in the implementation.

#### Libraries
import SQL, flask for use of databases and flask
import datetime, gmtime, strftime for formatting of timestamps
import json and urllib.request for obtaining data from Gemini API
import gemini to have access to python client that takes care of API connection and requests.
import threading to have access to threading. This is required for the implementation of stop loss. (Refer to section on stop loss function for details)

#### User specific details
Public and private API keys can be created at Gemini. For sandbox, create account from https://exchange.sandbox.gemini.com. For live, create account from https://gemini.com/.
Set of API keys are already configured in application.py for purpose of this project.

#### btc_price()
To obtain the latest Bitcoin price via Gemini's public data API. The returned json file is parsed and only the last price is stored for use.

#### index()
Shows Bitcoin price, balance, show trades, open orders, stop losses in 1 page.

##### 1) BTC price
Calls btc_price() to show latest price

##### 2) Balances
Calls get_balance() from external API client and store BTC & USD balances in variables for use.

##### 3) Trade History
Calls get_past_trades from external API client. A list of dictionaries is returned from Gemini. Loop through each record in the list, delete irrelevant keys and rename existing keys for 'nicer'
presentation in html table. Timestamp returned from Gemini is number of sec since UNIX epoch. Hence, need to convert using datetime function.
Finally, array is limited to 10 to optimise viewing on webpage.

##### 4) Open orders
Calls active_orders() from external API client. Similar operations to data as Trade History.

##### 5) Stop Losses
Select stop loss records from db.

##### 6) Orders cancellation
Uses POST method to get id of order to cancel from user. If cancel order is for open orders, push id to external API client for submission to Gemini. If cancel is for stop loss, delete from db.

#### trade()
Gets user input on buy or sell option, amount and price. Validate for valid inputs, and provide feedback via flash message on-screen. For buy orders, submit to Gemini via external API client. For Sell orders,
to check with current BTC price. If price is lower, store in db. If not, submit sell order in similar process to buy order.

#### stop_loss()
threading.timer specifies that the function is to be started every 2s. This is required as the stop loss records in db have to be compared to latest price constantly behind the scene to determine if stop loss price is hit.
2s interval seems logical considering the rate limits at Gemini and expected price volatility. The function gets stop loss records from db as a list and loops through each record. For each record, the stop loss price is
compared to latest btc price from btc_price(). A new order is submitted if stop loss price is >= btc price, which signifies a stop loss being hit. When that happens, that particular record gets deleted from db.

### finance.db
1 table named as 'stops', containing stop loss price and amount.

### index.html
Presents all data mentioned in application.py in different html tables.

### trade.html
Contains user input form for trade order submission. Flash message for to inform user of successful submission or errors included.

### Documentations and Critical Information
External API client: https://github.com/mtusman/gemini-python
GEMINI API doc: https://docs.gemini.com/
Sandbox URL: https://exchange.sandbox.gemini.com
Live URL: https://exchange.sandbox.gemini.com

### Citations
For API Client: https://github.com/mtusman/gemini-python
For Flask implementation and jinja template reference: CS50 pset

### Limitations and comments
The sandbox environment does not have the same price movements and liquidity as compared to real market. As such, orders may not get executed quick enough for effective end-to-end testing. However,
as long orders are submitted and reflected in the app correctly, it is logical to assume that the execution would be perfect in actuality since execution of submitted orders are a well-established process within Gemini.
