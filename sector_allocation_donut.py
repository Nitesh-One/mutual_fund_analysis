import pandas as pd
import plotly.express as px

holdings = pd.read_csv(
    "data/raw/09_portfolio_holdings.csv"
)

sector_weights = (
    holdings
    .groupby("sector")["weight_pct"]
    .sum()
    .reset_index()
)

sector_weights = sector_weights.sort_values(
    by="weight_pct",
    ascending=False
)

fig = px.pie(
    sector_weights,
    names="sector",
    values="weight_pct",
    title="Sector Allocation Across Equity Funds"
)

fig.update_traces(
    hole=0.4,
    textposition="inside",
    textinfo="percent+label"
)

fig.show()
