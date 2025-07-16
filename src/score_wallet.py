import joblib
import pandas as pd
import json
from utils.feature_engineering import build_features

def score_wallet(wallet_address, file_path, model_path):
    with open(file_path, 'r') as f:
        data = json.load(f)

    df = pd.DataFrame(data)
    df['actionData.amount'] = df['actionData'].apply(lambda x: float(x['amount']))
    df['actionData.assetSymbol'] = df['actionData'].apply(lambda x: x['assetSymbol'])

    df_wallet = df[df['userWallet'] == wallet_address]
    features = build_features(df_wallet)

    model = joblib.load(model_path)
    X = features[['total_actions', 'total_amount', 'unique_assets']]
    score = model.predict(X)[0]
    print(f"Wallet: {wallet_address}\nCredit Score: {round(score, 2)}")

if __name__ == "__main__":
    import sys
    score_wallet(sys.argv[1], "data/user-wallet-transactions.json", "models/credit_score_model.pkl")
