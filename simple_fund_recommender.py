import pandas as pd

funds = pd.read_csv(
    "data/processed/scheme_performance.csv"
)

risk_appetite = input(
    "Enter Risk Appetite (Low/Moderate/High): "
)

recommendations = (
    funds[
        funds["risk_grade"]
        .str.lower()
        ==
        risk_appetite.lower()
    ]
    .sort_values(
        "sharpe_ratio",
        ascending=False
    )
    .head(3)
)

recommendations = recommendations[
    [
        "scheme_name",
        "fund_house",
        "category",
        "sharpe_ratio",
        "return_3yr_pct"
    ]
]

print(
    "\nRecommended Funds:\n"
)

print(recommendations)
