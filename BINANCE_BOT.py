# General Functions
import websocket, json, config
from binance.client import Client
from binance.enums import *
from datetime import datetime
from MAIN_BOT import main_bot
from PORTFOLIO_DATA import import_trade_portfolio
from TRADE_BOOK_DATA import import_trade_book
from CHECK_ALL_DATA import check_all_data
from GET_MA import get_MA

#def binance_bot():
client = Client(config.API_KEY, config.API_SECRET)
SOCKET = "wss://stream.binance.com:9443/ws/etheur@kline_1m"
DATA_PERIOD = 100
RR = 1.4

all_data = check_all_data(DATA_PERIOD)

PORTFOLIO = import_trade_portfolio()
TRADE_BOOK = import_trade_book()
PORTFOLIO['ACTIVE_TRADES'] = len(TRADE_BOOK['BUY_PRICE'])
print(PORTFOLIO['ACTIVE_TRADES'])
print('RR: '+str(RR))

ETH_BALANCE = round(float(client.get_account()['balances'][2]['free']),6)
BUSD_BALANCE = round(float(client.get_account()['balances'][188]['free']),6)
EUR_BALANCE = round(float(client.get_account()['balances'][197]['free']),9)

PORTFOLIO['Balance_1'] = ETH_BALANCE
PORTFOLIO['Balance_2'] = EUR_BALANCE

TEST = True
#revert import TRADE BOOK!!!

if TEST:

    import pandas as pd
    print('Starting Test')

    #all_ticker_data = pd.read_csv("testData/ETHEUR-1m-2021-06-08.csv")
    all_ticker_data = pd.read_csv("testData/ETHEUR-1m-2021-07.csv")

    raw_data = []

    for x in range(len(all_ticker_data)):
        data = {'k': {
                    'o': all_ticker_data['o'][x],
                    'c': all_ticker_data['c'][x],
                    'h': all_ticker_data['h'][x],
                    'l': all_ticker_data['l'][x],
                    'x': all_ticker_data['x'][x],
                    'T': all_ticker_data['date'][x]
                    }}
        raw_data.append(data)


    for i in range(len(raw_data)):
        main_bot(raw_data[i], PORTFOLIO, TRADE_BOOK, DATA_PERIOD, all_data, RR, True)
        print(str(i))

else:

    def on_open(ws):
            print('Opened connection')

    def on_close(ws):
        print('closed connection')

    def on_message(ws, message):
        raw_data = json.loads(message)

        try:
            main_bot(raw_data, PORTFOLIO, TRADE_BOOK, DATA_PERIOD, all_data, RR, False)
        except Exception as e:
            print("Main issue - {}".format(e))

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        SHORT_MA = get_MA(all_data['close'])
        print(raw_data['k']['c']+' - ',str(SHORT_MA[-1])+' - ', current_time, ' - Active Trades: '+str(len(TRADE_BOOK['BUY_PRICE'])))

ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
websocket.setdefaulttimeout(5)
ws.run_forever()                
