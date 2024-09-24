# main_operations.py

import yfinance as yf
import numpy as np
from sklearn.linear_model import LinearRegression

def get_historical_data(ticker='AAPL', period='1y'):
    stock = yf.Ticker(ticker)
    hist_data = stock.history(period=period)
    return hist_data

def get_real_time_price(ticker='AAPL'):
    stock = yf.Ticker(ticker)
    price = stock.history(period='1d')['Close'].iloc[-1]
    return price

def train_model(data):
    X = np.array(range(len(data))).reshape(-1, 1)  # Example feature: time
    y = data['Close'].values  # Target: stock prices
    model = LinearRegression()
    model.fit(X, y)
    return model

def predict_future(model, future_days=10):
    last_day = len(model.coef_)  # Get last known data point
    future = np.array(range(last_day, last_day + future_days)).reshape(-1, 1)
    return model.predict(future)
