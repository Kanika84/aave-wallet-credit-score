import json
import pandas as pd
import numpy as np
import os
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from math import sqrt

from src.feature_engineering import create_features

def load_data(json_path):
    with open(json_path, "r") as f:
        data = json.load(f)
    return pd.DataFrame(data)

def train(json_path, model_path):
    df = load_data(json_path)
    df = create_features(df)

    X = df.drop(columns=["userWallet", "creditScore"])
    y = df["creditScore"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump(model, model_path)

    print("Model trained and saved to", model_path)
    print("RMSE:", sqrt(mean_squared_error(y_test, model.predict(X_test))))

if __name__ == "__main__":
    train("data/user-wallet-transactions.json", "models/credit_score_model.pkl")
