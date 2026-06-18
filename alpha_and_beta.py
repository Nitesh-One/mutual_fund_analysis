from scipy.stats import linregress
import pandas as pd

fund = pd.read_csv(
    "data/processed/nav_daily_returns.csv"
)

fund["date"] = pd.to_datetime(
    fund["date"]
)

nifty = pd.read_csv(
    "data/raw/10_benchmark_indices.csv"
)

nifty = nifty[
    nifty["index_name"] == "NIFTY100"
].copy()

nifty = nifty.sort_values("date")

nifty["benchmark_return"] = (
    nifty["close_value"]
    .pct_change()
)

nifty["date"] = pd.to_datetime(
    nifty["date"]
)

results = []


for amfi_code, group in fund.groupby(
    "amfi_code"
):
    merged = pd.merge(
        group,
        nifty,
        on="date",
        how="inner",
        validate="one_to_one"
    )
    merged = merged.dropna(
        subset=[
            "benchmark_return",
            "daily_return"
        ]
    )

    regression = linregress(
        merged["benchmark_return"],
        merged["daily_return"]
    )
    
    beta = regression.slope
    
    daily_alpha = regression.intercept    
    
    alpha = daily_alpha * 252
    
    results.append({
        "amfi_code": amfi_code,
        "alpha": alpha,
        "beta": beta,
        "r_squared":
            regression.rvalue ** 2
    })
    
alpha_beta = pd.DataFrame(
    results
)

print(alpha_beta.head())

alpha_beta.to_csv(
    "data/processed/fund_alpha_beta.csv",
    index=False
)    
    