import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(
    "data/processed/cleaned_investor_transactions.csv"
)

sip_df = df[
    df["transaction_type"] == "SIP"
]

state_sip = (
    sip_df.groupby("state")["amount_inr"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10,6))

sns.barplot(
    x=state_sip.values,
    y=state_sip.index
)

plt.title("SIP Amount by State")
plt.xlabel("Total SIP Amount (₹)K")
plt.ylabel("State")

plt.tight_layout()
plt.show()
