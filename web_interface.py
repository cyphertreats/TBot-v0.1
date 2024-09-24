from flask import Flask, render_template, jsonify
import data_fetcher
import model

app = Flask(__name__)

@app.route('/')
def home():
    hist_data = data_fetcher.get_historical_data()
    trained_model = model.train_model(hist_data)
    future_prediction = model.predict_future(trained_model)
    return render_template('index.html', predictions=future_prediction)

if __name__ == '__main__':
    app.run(debug=True)
