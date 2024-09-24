# web_interface.py

from flask import Flask, render_template, jsonify
import main_operations  # Import the new operations module

app = Flask(__name__)

@app.route('/')
def home():
    hist_data = main_operations.get_historical_data()  # Call from main_operations
    trained_model = main_operations.train_model(hist_data)
    future_prediction = main_operations.predict_future(trained_model)

    # Convert future_prediction from NumPy array to list
    future_prediction_list = future_prediction.tolist()

    return render_template('index.html', predictions=future_prediction_list)

if __name__ == '__main__':
    app.run(debug=True)
