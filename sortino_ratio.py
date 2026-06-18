import pandas as pd
import numpy as np

df = pd.read_csv(
    "data/processed/nav_daily_returns.csv"
)

rf_daily = 0.065 / 252

results = []

for amfi_code, group in df.groupby("amfi_code"):

    returns = group["daily_return"].dropna()

    mean_return = returns.mean()

    # Only negative returns
    downside_returns = returns[
        returns < 0
    ]

    downside_std = downside_returns.std()

    if (
        pd.isna(downside_std)
        or downside_std == 0
    ):
        sortino = np.nan
    else:
        sortino = (
            (mean_return - rf_daily)
            / downside_std
        ) * np.sqrt(252)

    results.append({
        "amfi_code": amfi_code,
        "avg_daily_return": mean_return,
        "downside_std": downside_std,
        "sortino_ratio": sortino
    })
    
sortino_df = pd.DataFrame(results)

sortino_df = sortino_df.sort_values(
    by="sortino_ratio",
    ascending=False
)

sortino_df["rank"] = range(
    1,
    len(sortino_df) + 1
)

print(
    sortino_df[
        [
            "rank",
            "amfi_code",
            "sortino_ratio"
        ]
    ].head(10)
)

sortino_df.to_csv(
    "data/processed/fund_sortino_ranking.csv",
    index=False
)
    