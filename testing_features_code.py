import yfinance as yf
from data_loader import DataEngine
symbol = 'AAPL'
stock_prices = yf.download(
							tickers = symbol,
                            period="7d")
#price = stock_prices.info['regularMarketPrice']
#print (stock_prices)

supriver = DataEngine(7,90,0,0,"dictionaries/data_dictionary.npy",0.05,100,1,0.05,symbol,"yahoo_finance")

stock_price_data, future_prices, not_found = supriver.get_data(symbol)
stock_price_data=stock_price_data['Open']
#stock_price_data=stock_price_data.reset_index(drop=True)
print (stock_price_data.iloc[-1])
