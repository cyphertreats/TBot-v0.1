from sklearn.linear_model import LinearRegression
import numpy as np

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
