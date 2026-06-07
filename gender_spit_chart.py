import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(
    "data/processed/cleaned_investor_transactions.csv"
)

plt.figure(figsize=(8,5))

sns.countplot(
    data=df,
    x="gender"
)

plt.title("Gender Distribution of Investors")
plt.xlabel("Gender")
plt.ylabel("Number of Investors")

plt.tight_layout()
plt.show()
