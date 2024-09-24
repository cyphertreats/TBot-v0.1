import yfinance as yf

def get_historical_data(ticker='AAPL', period='1y'):
    stock = yf.Ticker(ticker)
    hist_data = stock.history(period=period)
    return hist_data

def get_real_time_price(ticker='AAPL'):
    stock = yf.Ticker(ticker)
    price = stock.history(period='1d')['Close'].iloc[-1]
    return price
