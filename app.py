from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import random
import datetime
import yfinance as yf
from statsmodels.tsa.arima.model import ARIMA
import pandas as pd
import warnings

app = Flask(__name__)
CORS(app)

warnings.filterwarnings("ignore")

def get_bert_sentiment(stock_symbol):
    print(f"Simulating BERT sentiment for: {stock_symbol}")
    sentiments = {
        "Positive": "Up",
        "Negative": "Down",
        "Neutral": "Neutral"
    }
    sentiment_label = random.choice(list(sentiments.keys()))
    trend_prediction = sentiments[sentiment_label]
    sentiment_score = random.uniform(0.7, 1.0)
    sentiment_string = f"{sentiment_label} ({sentiment_score:.2f})"
    return sentiment_string, trend_prediction

def get_model_prediction(stock_symbol):
    print(f"Fetching data from Yahoo Finance for: {stock_symbol}")
    
    try:
        stock_data = yf.download(stock_symbol, period="1y", interval="1d")
        if stock_data.empty:
            raise Exception("No data found for symbol.")
        
        # --- THIS IS THE NEW LINE THAT FIXES THE BUG ---
        stock_data.index = pd.to_datetime(stock_data.index)
        # --------------------------------------------------

    except Exception as e:
        print(f"Error fetching data: {e}")
        return None, None, "Error: Invalid stock symbol or no data."

    try:
        print("Training ARIMA model...")
        model_data = stock_data['Close'].astype(float)
        
        model = ARIMA(model_data, order=(6, 1, 0))
        model_fit = model.fit()
        
        print("Forecasting...")
        forecast_steps = 3
        forecast_result = model_fit.forecast(steps=forecast_steps)
        
        history = {"dates": [], "prices": []}
        forecast = {"dates": [], "prices": []}
        

        last_30_days = model_data.tail(30)
        # Ensure the index is datetime-like and format dates safely
        last_30_index = pd.to_datetime(last_30_days.index)
        for date, price in zip(last_30_index, last_30_days.values):
            history["dates"].append(pd.Timestamp(date).strftime("%Y-%m-%d"))
            history["prices"].append(round(float(price), 2))

        # Use a datetime-like last real date so adding timedeltas is safe
        last_real_date = pd.to_datetime(model_data.index[-1])
        for i in range(forecast_steps):
            next_date = last_real_date + datetime.timedelta(days=i + 1)
            forecast["dates"].append(pd.Timestamp(next_date).strftime("%Y-%m-%d"))
            forecast["prices"].append(round(float(forecast_result.iloc[i]), 2))

        return history, forecast, None
        
    except Exception as e:
        print(f"Error during model training/forecasting: {e}")
        return None, None, "Error: Could not process data."


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def handle_prediction():
    data = request.get_json()
    stock_symbol = data.get('symbol')
    
    if not stock_symbol:
        return jsonify({"error": "No stock symbol provided"}), 400

    print(f"--- Processing request for: {stock_symbol} ---")

    sentiment_result, trend_result = get_bert_sentiment(stock_symbol)
    history_data, forecast_data, error = get_model_prediction(stock_symbol)
    
    if error:
        return jsonify({"error": error}), 400

    response_data = {
        "prediction_trend": trend_result,
        "sentiment_score": sentiment_result,
        "history": history_data,
        "forecast": forecast_data
    }
    
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
