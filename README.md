# 🧠 Aave Wallet Credit Scoring

This project builds a machine learning model to assign a **credit score (0–1000)** to each wallet interacting with the **Aave V2 protocol** on **Polygon**, using only historical transaction behavior.

---

## 🚀 Problem Statement

You are provided with 100K raw transaction-level records from the Aave V2 protocol.

Each entry includes:

- Wallet address
- Action (`deposit`, `borrow`, `repay`, `redeemunderlying`, `liquidationcall`)
- Token, USD value, timestamp

> Your task: Predict a **credit score between 0 and 1000** per wallet, where:
> - Higher = trustworthy, responsible, consistent usage
> - Lower = bot-like, exploitative, risky behavior

---

## 🏗️ Project Architecture

aave-wallet-credit-score/
├── data/
│ └── user-wallet-transactions.json
├── models/
│ └── credit_score_model.pkl
├── reports/
│ └── analysis.md
├── src/
│ ├── parser.py
│ ├── feature_engineering.py
│ ├── model_utils.py
│ ├── train_model.py
│ └── score_wallets.py
└── README.md

yaml
Copy
Edit

---

## 🧪 Features Engineered

| Feature                 | Description                                 |
|------------------------|---------------------------------------------|
| total_actions          | Total number of transactions per wallet     |
| total_deposit_usd      | Normalized USD value of deposits            |
| total_borrow_usd       | Total borrow volume                         |
| num_unique_assets      | Distinct tokens interacted with             |
| num_liquidations       | Times wallet got liquidated                 |
| avg_tx_gap_days        | Avg time (days) between transactions        |
| active_days            | Span between first & last tx (days)         |
| net_flow               | Deposits - Withdrawals (USD)                |

---

## 🔍 Model Training & Scoring

We use a **Random Forest Regressor** trained on heuristically-labeled scores from the above features. Scores are then:

- Normalized to **0–1000**
- Stored in `wallet_scores.csv`

> Training code: `python src/train_model.py`

---

## 📜 How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
2. Train the model
bash
Copy
Edit
python -m src.train_model
3. Generate credit scores
bash
Copy
Edit
python -m src.score_wallets
Output will be saved in: wallet_scores.csv

✅ Deliverables
✅ README.md: architecture, pipeline, features

✅ analysis.md: score distribution and behavior

✅ wallet_scores.csv: final credit scores per wallet

👨‍💻 Author
Kanika Sikka
