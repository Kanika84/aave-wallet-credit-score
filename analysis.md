Wallet Score Analysis – Aave V2 Protocol

This file summarizes the results of the machine learning model that scores user wallets between **0 and 1000** based on their historical interaction behavior with Aave V2.

---

## 📌 Score Distribution

| Score Range | Number of Wallets | Remarks                         |
|-------------|-------------------|----------------------------------|
| 0–100       | 18                | Inactive, exploitative or bots   |
| 100–200     | 39                | Low volume, short span usage     |
| 200–300     | 54                | Some usage but poor repayment    |
| 300–400     | 73                | Limited diversity of behavior    |
| 400–500     | 62                | Balanced but low-frequency use   |
| 500–600     | 47                | Decent deposits, low risk        |
| 600–700     | 28                | Moderate activity, consistent    |
| 700–800     | 19                | Trusted, long-term use           |
| 800–900     | 9                 | Strong credit-worthy behavior    |
| 900–1000    | 3                 | DeFi-native power users          |

📊 **Total wallets scored:** 352

---

## 🔬 Behavioral Insights

### 🔴 Low-Scoring Wallets (0–300)
- Performed only 1 or 2 actions (often `redeemunderlying`)
- Assets used: mostly **USDC only**
- Many had no deposit but only withdrawals — suspicious
- Could be:
  - Test wallets
  - Bots draining incentives
  - Exploit attempts

### 🟢 High-Scoring Wallets (700–1000)
- High total volume transacted
- Long wallet lifespan (months between 1st and last tx)
- Diverse token activity (USDC, WMATIC, DAI)
- Minimal liquidation events

---

## 🧠 Feature Influence

| Feature             | Contribution |
|--------------------|--------------|
| total_deposit_usd  | Very High    |
| active_days        | High         |
| num_liquidations   | Negative     |
| num_unique_assets  | Moderate     |
| borrow/repay ratio | High         |

---

## 📈 Score Visualization

> _Created using matplotlib and seaborn_

- **Histogram** of scores in bins of 100
- **Bar chart** of actions per score group
- **Scatter plot**: deposit amount vs. credit score

---

## 📍 Limitations

- Lacks off-chain behavioral indicators
- Small number of `borrow` and `repay` events in the dataset
- No labels (e.g., fraud/scam) to validate score quality

---

## 🔮 Future Improvements

- Add clustering to segment wallet types
- Integrate cross-chain reputation (ENS, POAP, Gitcoin)
- Build dashboard for score monitoring

---

👨‍💻 Author: Kanika Sikka  
Assignment: Wallet Credit Scoring – Aave V2 Protocol 
