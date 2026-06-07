# Road Accident Forecasting & Risk Analytics
# Run the forecasting pipeline

from src.data_loader import load_data
from src.preprocessing import preprocess
from src.train_sarima import train_sarima
from src.train_lstm import train_lstm
from src.evaluate import evaluate_model

if __name__ == "__main__":
    df = load_data()
    df = preprocess(df)
    sarima_model = train_sarima(df)
    lstm_model = train_lstm(df)
    evaluate_model(sarima_model, lstm_model, df)
    print("Pipeline complete.")
