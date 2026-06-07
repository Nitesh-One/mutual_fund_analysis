import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "data/processed/cleaned_investor_transactions.csv"
)

tier_counts = (
    df["city_tier"]
    .value_counts()
)

plt.figure(figsize=(7,7))

plt.pie(
    tier_counts,
    labels=tier_counts.index,
    autopct="%1.1f%%"
)

plt.title("T30 vs B30 City Tier Distribution")

plt.show()
