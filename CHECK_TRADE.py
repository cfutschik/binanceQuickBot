from CHECK_ENTRY import check_entry
import EXECUTE_TRADE
import GET_ATR

def check_trade(PORTFOLIO, TRADE_BOOK, all_data, moving_price, RR, TEST):

    if PORTFOLIO["ACTIVE_TRADES"] < 7:
        if PORTFOLIO["BUY_HOLD"] == 0:
            if check_entry(all_data):

                ATR = GET_ATR.get_ATR(all_data, 14)
                stop_loss = all_data['low'][-1]-ATR
                sell_marker = (all_data['close'][-1]-stop_loss)*RR+all_data['close'][-1]

                gain_threshold = sell_marker/all_data['close'][-1]

                if gain_threshold > 0.18: #accounts for binance fees
                                            
                    EXECUTE_TRADE.execute_buy(PORTFOLIO, TRADE_BOOK, all_data, ATR, stop_loss, sell_marker, TEST)

    if PORTFOLIO["ACTIVE_TRADES"] != 0:
        
        if TEST == True:
            i = 0
            while i < len(TRADE_BOOK['BUY_PRICE']):
                #print('Sell loop: '+str(len(TRADE_BOOK['BUY_PRICE'])))
                #Fixed Stop Loss
                if all_data['low'][-1] <= TRADE_BOOK["STOP_LOSS"][i]:
                    EXECUTE_TRADE.execute_sell(TRADE_BOOK['STOP_LOSS'][i], PORTFOLIO, TRADE_BOOK, i, TEST)

                elif all_data['high'][-1] >= TRADE_BOOK["SELL_MARKER"][i]:
                    EXECUTE_TRADE.execute_sell(TRADE_BOOK["SELL_MARKER"][i], PORTFOLIO, TRADE_BOOK, i, TEST)
                
                else:
                    i+=1

        else:

            i = 0
            while i < len(TRADE_BOOK['BUY_PRICE']):
                #print('Sell loop: '+str(len(TRADE_BOOK['BUY_PRICE'])))
                #Fixed Stop Loss
                if moving_price <= TRADE_BOOK["STOP_LOSS"][i]:
                    EXECUTE_TRADE.execute_sell(moving_price, PORTFOLIO, TRADE_BOOK, i, TEST)

                elif moving_price >= TRADE_BOOK["SELL_MARKER"][i]:
                    EXECUTE_TRADE.execute_sell(moving_price, PORTFOLIO, TRADE_BOOK, i, TEST)
                
                else:
                    i+=1
