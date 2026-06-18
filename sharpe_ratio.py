import pandas as pd
import numpy as np

df = pd.read_csv(
    "data/processed/nav_daily_returns.csv"
)

df["date"] = pd.to_datetime(df["date"])

rf_daily = 0.065 / 252

results = []

for amfi_code, group in df.groupby("amfi_code"):

    returns = group["daily_return"].dropna()

    mean_return = returns.mean()

    std_return = returns.std()

    if std_return == 0:
        sharpe = np.nan
    else:
        sharpe = (
            (mean_return - rf_daily)
            / std_return
        ) * np.sqrt(252)

    results.append({
        "amfi_code": amfi_code,
        "avg_daily_return": mean_return,
        "volatility": std_return,
        "sharpe_ratio": sharpe
    })
    
sharpe_df = pd.DataFrame(results)

sharpe_df = sharpe_df.sort_values(
    by="sharpe_ratio",
    ascending=False
)

sharpe_df["rank"] = range(
    1,
    len(sharpe_df) + 1
)    

sharpe_df = pd.DataFrame(results)

sharpe_df = sharpe_df.sort_values(
    by="sharpe_ratio",
    ascending=False
)

sharpe_df["rank"] = range(
    1,
    len(sharpe_df) + 1
)

print(
    sharpe_df[
        [
            "rank",
            "amfi_code",
            "sharpe_ratio"
        ]
    ].head(10)
)

sharpe_df.to_csv(
    "data/processed/fund_sharpe_ranking.csv",
    index=False
)
