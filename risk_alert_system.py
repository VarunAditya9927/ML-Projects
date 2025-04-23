import pandas as pd

# Load transaction data
df = pd.read_csv("transactions.csv")

# Define flagging logic
flagged = df[(df['amount'] > 9000) & (df['risk_level'] == 'High')]

# Save flagged transactions
flagged.to_csv("flagged_transactions.csv", index=False)

print("Flagged Transactions:")
print(flagged)
