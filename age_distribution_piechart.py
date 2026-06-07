import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/cleaned_investor_transactions.csv")

age_counts = df["age_group"].value_counts()

plt.figure(figsize=(8,8))

plt.pie(
    age_counts,
    labels=age_counts.index,
    autopct="%1.1f%%"
)

plt.title("Investor Age Group Distribution")

plt.show()
