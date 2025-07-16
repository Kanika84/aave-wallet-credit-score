🧠 Aave Wallet Credit Scoring – ML Pipeline

This project builds a machine learning pipeline to assign **DeFi credit scores (0–1000)** to wallets interacting with the **Aave V2 protocol on the Polygon network**, using historical transaction behavior.

---

## 🛠️ Tech Stack

| Layer         | Tool/Library                    |
| ------------- | ------------------------------- |
| Language      | Python 3.9+                     |
| Data Handling | Pandas, JSON                    |
| ML Model      | Scikit-learn (Random Forest)    |
| Deployment    | CLI (Python script)             |
| Storage       | Local `.pkl` model + JSON input |
| Visualization | Jupyter Notebook (matplotlib)   |

---

## 📈 Project Goal

Assign a **credit score between 0–1000** to each wallet based on:

- Deposit frequency & volume
- Withdraw/redemption activity
- Asset diversity
- Wallet activity duration

The higher the score, the more **trustworthy**, **active**, and **repayment-oriented** the wallet behavior appears.

---

## 🧪 Features Engineered

| Feature        | Description                              |
| -------------- | ---------------------------------------- |
| total_actions  | Total number of actions taken            |
| total_amount   | Total amount transacted (USD normalized) |
| unique_assets  | Number of unique assets used             |
| score (target) | Heuristic score for ML training          |

---

## 🧮 Credit Score Logic

We train a simple regression model (`RandomForestRegressor`) using a composite heuristic score and normalize it to a 0–1000 range.

> Scores are saved to `wallet_scores.csv`

---

## 🚀 How to Run

### 1. Clone & Install

````bash
git clone https://github.com/Kanika84/aave-wallet-credit-score.git
cd aave-wallet-credit-score
pip install -r requirements.txt
2. Add Your Data
Place user-wallet-transactions.json into the data/ folder.

3. Train the Model
bash
Copy code
python -m src.train_model
4. Score a Wallet
bash
Copy code
python -m src.score_wallet 0xabc1234...your_wallet
5. View Scores
bash
Copy code
cat wallet_scores.csv
🖼️ Screenshots
Wallet Scoring	Credit Score Distribution

🔬 What I'd Improve Next
Add clustering or anomaly detection (bot detection)

Incorporate liquidation/repayment data (not yet fully parsed)

Build REST API / dashboard (Flask + React)

Export scores to MongoDB for dApps

⏱️ Time Spent
~5 hours: data parsing, feature engineering, ML training, CLI testing, README/report creation.

👨‍⚖️ License
MIT License

🧑‍💻 Author
Kanika Sikka

yaml
Copy code

---

## ✅ `reports/analysis.md`

```markdown
# 📊 Credit Score Analysis Report

This report provides an analysis of the scores assigned to wallets using the trained ML model.

---

## 🔢 Score Distribution

| Score Range | Wallet Count |
|-------------|--------------|
| 0–100       | 3            |
| 100–200     | 12           |
| 200–300     | 21           |
| 300–400     | 43           |
| 400–500     | 56           |
| 500–600     | 71           |
| 600–700     | 49           |
| 700–800     | 32           |
| 800–900     | 18           |
| 900–1000    | 8            |

> 📌 Total wallets scored: 313

---

## 🧠 Observations

### ✅ High Scoring Wallets (800–1000)
- Performed regular deposits in multiple assets (USDC, WMATIC)
- Very active over time (long wallet lifetime)
- High deposit-to-redeem ratios (net positive position)

### ⚠️ Low Scoring Wallets (0–200)
- Performed only 1–2 interactions
- Redeemed more than deposited
- Mostly interacted with a single asset

---

## 📉 Visualizations

### Credit Score Histogram
![Histogram](screenshot2.png)

### Asset Usage Heatmap
![Heatmap](heatmap.png)

---

## 🛠️ Next Steps for Deeper Insights
- Analyze liquidation, repay, borrow events
- Time-series activity clustering (seasonality, bursts)
- Compare with known scam/bot lists

---

Generated with ❤️ by Kanika Sikka
````
