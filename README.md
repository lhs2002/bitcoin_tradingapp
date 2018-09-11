# Usage Manual for Gemini Trading App
This manual serves as an operation guide for users. Refer to DESIGN.md for code level descriptions.

## Introduction
The main objective for this application is to provide a convenient way to trade Bitcoin on the Gemini Exchange(https://gemini.com/), which is one of the most popular and reliable Bitcoin exchanges
in existence. Through the app, user will be able to obtain Bitcoin pricing, view balances, trade history and submit Buy/Sell orders. Specifically,
the highlight of the app is the ability to submit stop loss orders, which is currently not supported natively by Gemini.

## Requirements to operate
This web app utilizes flask and jinja templates to serve webpages accessable by browsers.

For purpose of testing and evaulation of this project, the app is already configured to connect to Gemini's sandbox environment using valid test API keys. In actuality for live usage, user will be required to
obtain an actual Gemini account with API keys and change configured url within the app.

Install gemini library--> pip install gemini_python as application requires this for connections.

To run, start flask and open output url.

## Features
All features described in below sections are available via Home and Trade pages. Data shown for these features are updated upon refresh of page.
User can refer to the last updated timestamp to know when data was last updated.

### Current Price
The latest Bitcoin traded price at Gemini is shown at the top of the Home Page.

### My Balances
User's Bitcoin and USD balance from Gemini is shown at the Home Page.

### Trade History
User's last 10 executed trades on Gemini are shown at the Home Page.

### Open Buy/Sell Orders
User's submitted buy and sell orders that are submitted to Gemini are shown at the Home Page. Note that these orders are yet to be filled/executed. Executed orders
are trades and are shown within Trade History.

Open orders can be canceled by providing the order id.


### Open Stop Losses
User's submitted stop loss orders are shown at the Home Page. Once triggered, a sell order is submitted to Gemini for execution and the order can be seen at the Open Buy/Sell Orders section.

Open stop losses can be canceled by providing the Stop loss no.

### Submitting trade orders
User can submit trade orders via the Trade Page. Choose Buy/Sell, the amount of BTC and the price of execution. A message will be flashed for successful order submission. In case where there are errors,
a message will also state the nature of the error.

Note: By definition, buy price has to be lower or equal to latest price. If sell price is lower than latest price, its a stop loss, else its a normal sell limit order.

