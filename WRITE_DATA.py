import csv

def write_sell(TRADE_BOOK, i):
    with open('dataFiles/TRADES.csv', 'a', newline='') as f:
        data_writer = csv.writer(f, delimiter=',',quoting=csv.QUOTE_MINIMAL)

        #print("flag 2: "+str(i))
        #print(TRADE_BOOK['TIME'][i])
        #print(TRADE_BOOK['BUY_PRICE'][i])
        #print(TRADE_BOOK['SELL_MARKER'][i])
        #print(TRADE_BOOK['STOP_LOSS'][i])
        #print(TRADE_BOOK['ATR'][i])
        #print(TRADE_BOOK['SELL_PRICE'][i])
        #print(TRADE_BOOK['GAIN'][i])

        #print("flag 2.a")

        data_writer.writerow([TRADE_BOOK['TIME'][i],
                              TRADE_BOOK['BUY_PRICE'][i],
                              TRADE_BOOK['SELL_MARKER'][i],
                              TRADE_BOOK['STOP_LOSS'][i],
                              TRADE_BOOK['ATR'][i],
                              TRADE_BOOK['SELL_PRICE'][i],
                              TRADE_BOOK['GAIN'][i]])

        #print("flag 3")

def write_candlestick_data(all_data):
    
    with open('dataFiles/candle_stick_data.csv', 'a', newline='') as f:
        data_writer = csv.writer(f, delimiter=',',quoting=csv.QUOTE_MINIMAL)

        data_writer.writerow([all_data['date'][-1],
                            all_data['high'][-1], 
                            all_data['low'][-1],
                            all_data['open'][-1], 
                            all_data['close'][-1],
                            all_data['20_MA'][-1]])

        

            



