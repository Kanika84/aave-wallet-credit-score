Wallet Credit Score Analysis

This document provides a detailed analysis of how wallet scores were assigned and distributed across the DeFi users interacting with the Aave V2 protocol on Polygon.

---

## 🎯 Objective

To analyze and interpret the behavior of wallets based on transaction-level interaction history, and assign each wallet a **credit score between 0–1000**, where:

- **High scores** (700–1000) indicate stable, frequent, and diversified activity.
- **Low scores** (0–300) may indicate risky, low-engagement, or bot-like behavior.

---

## 📈 Score Distribution

| Score Range | Number of Wallets | Description                        |
| ----------- | ----------------- | ---------------------------------- |
| 0–100       | 9                 | Minimal/no deposits, likely bots   |
| 100–200     | 24                | Sparse activity                    |
| 200–300     | 41                | Single asset, low deposit          |
| 300–400     | 52                | Low-to-moderate activity           |
| 400–500     | 63                | Average activity, low diversity    |
| 500–600     | 48                | Moderate volume, good consistency  |
| 600–700     | 33                | Solid behavior, multiple assets    |
| 700–800     | 20                | Consistent, high-value wallets     |
| 800–900     | 12                | Highly trustworthy & diverse usage |
| 900–1000    | 5                 | Top-performing, DeFi native users  |

> 📦 Sample Size: 307 wallets from parsed dataset.

---

## ✅ High Score Wallet Characteristics

Wallets in the **800–1000** range typically showed:

- Frequent **deposit** transactions
- Minimal or no **redeemunderlying** (withdraw) actions
- Interacted with **3 or more unique assets**
- Consistent behavior over a span of months

✅ These are likely long-term DeFi users or institutions.

---

## ⚠️ Low Score Wallet Characteristics

Wallets scoring between **0–300** showed:

- Only **1–2 transactions** total
- Primarily **redeemwithout deposit**, i.e., outbound only
- Low overall USD value (< $5 total)
- Activity clustered in a few blocks (bot-like)

⚠️ These wallets are considered risky or irrelevant for lending trust scores.

---

## 🧠 Feature Importance (via Random Forest)

| Feature       | Importance (%) |
| ------------- | -------------- |
| total_amount  | 52.3%          |
| total_actions | 32.1%          |
| unique_assets | 15.6%          |

> Deposit volume and transaction count were the strongest predictors.

---

## 🖼️ Visualization (Jupyter Notebook)

- 📊 Histogram of score distribution
- 🟢 Scatter: total_amount vs credit_score
- 🔵 Heatmap of action types per score range

_(Refer to `notebooks/data_analysis.ipynb` for interactive plots)_

---

## 📌 Limitations

- Doesn't include borrow/repay/liquidation (future work)
- Manual heuristic used for training score — could be biased
- No off-chain identity or historical defaults used

---

## 🚀 Future Work

- Integrate **borrow + repay** behavior
- Use **unsupervised clustering** to detect anomalous bots
- Serve scores via API for real-time DeFi credit monitoring

---

Generated as part of Take-Home Assignment – SDE  
🧑‍💻 Author: Kanika Sikka
