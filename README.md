# 🛡️ Risk Alert System

This project simulates a basic transaction monitoring system used in risk and compliance analytics. It scans transactional data and flags high-risk transactions based on amount thresholds and customer risk levels.

## 🔍 Project Goal
Identify potentially suspicious activity that could indicate fraud or AML concerns.

## 📂 Files Included
- `transactions.csv`: Sample dataset with synthetic transaction records
- `risk_alert_system.py`: Python script that flags risky transactions
- `flagged_transactions.csv`: Output file listing all flagged records

## ⚙️ Logic Used
- Flag any transaction where:
  - `amount > $9000` **AND**
  - `risk_level == 'High'`

## 🧰 Tools Used
- Python (pandas)
- CSV files for simplicity

## 📈 Result
Out of 10 transactions, high-risk ones are flagged and exported into `flagged_transactions.csv`.

## 🧪 How to Run
```bash
python risk_alert_system.py
```

The output will be printed and saved to a new CSV file.

---
*Created by Varun Aditya Madala*
