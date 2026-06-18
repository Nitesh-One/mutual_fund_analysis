import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

nav = pd.read_csv(
    "data/processed/cleaned_nav_history.csv"
)

nav["date"] = pd.to_datetime(nav["date"])

nav = nav.sort_values(
    by=["amfi_code", "date"]
)

nav["daily_return"] = (
    nav.groupby("amfi_code")["nav"]
       .pct_change()
)

print(
    nav[
        ["amfi_code", "date", "nav", "daily_return"]
    ].head(10)
)

print(
    nav["daily_return"].describe()
)



plt.figure(figsize=(10,6))

sns.histplot(
    nav["daily_return"],
    bins=50,
    kde=True
)

plt.title(
    "Distribution of Daily Returns"
)

plt.xlabel("Daily Return")
plt.ylabel("Frequency")

plt.show()


print(
    nav["daily_return"].nlargest(10)
)

print(
    nav["daily_return"].nsmallest(10)
)


nav.to_csv(
    "data/processed/nav_daily_returns.csv",
    index=False
)
