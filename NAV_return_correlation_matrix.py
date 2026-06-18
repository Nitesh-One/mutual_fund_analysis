import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

nav = pd.read_csv(
    "data/processed/cleaned_nav_history.csv"
)

nav["date"] = pd.to_datetime(nav["date"])

selected_funds = [
    119551,  # SBI Bluechip
    120503,  # ICICI Bluechip
    118632,  # Nippon Large Cap
    119092,  # Axis Bluechip
    120841,  # Kotak Bluechip
    125497,
    120716,
    118989,
    119164,
    120825
]

nav = nav[
    nav["amfi_code"].isin(selected_funds)
]

nav_matrix = nav.pivot(
    index="date",
    columns="amfi_code",
    values="nav"
)

nav_matrix = nav.pivot(
    index="date",
    columns="amfi_code",
    values="nav"
)

daily_returns = (
    nav_matrix.pct_change()
)

corr_matrix = (
    daily_returns.corr()
)


plt.figure(figsize=(10,8))

sns.heatmap(
    corr_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title(
    "NAV Return Correlation Matrix"
)

plt.tight_layout()
plt.show()
