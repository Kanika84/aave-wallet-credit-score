import pandas as pd

def build_features(df):
    grouped = df.groupby('userWallet').agg(
        total_actions=('action', 'count'),
        total_amount=('actionData.amount', 'sum'),
        unique_assets=('actionData.assetSymbol', pd.Series.nunique),
    ).reset_index()
    return grouped
