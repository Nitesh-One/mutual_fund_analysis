import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data/processed/cleaned_investor_transactions.csv")
sip_df = df[df["transaction_type"] == "SIP"]

plt.figure(figsize=(10,6))

sns.boxplot(
    data=sip_df,
    x="age_group",
    y="amount_inr"
)

plt.title("SIP Amount Distribution by Age Group")
plt.xlabel("Age Group")
plt.ylabel("SIP Amount (₹)")

plt.show()
