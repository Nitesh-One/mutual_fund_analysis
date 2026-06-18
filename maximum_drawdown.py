import pandas as pd

nav = pd.read_csv(
    "data/processed/cleaned_nav_history.csv"
)

nav["date"] = pd.to_datetime(
    nav["date"]
)

nav = nav.sort_values(
    ["amfi_code", "date"]
)

results = []

for amfi_code, group in nav.groupby(
    "amfi_code"
):
    group = group.copy()

    group["running_max"] = (
        group["nav"]
        .cummax()
    )
    
    group["drawdown"] = (
        group["nav"]
        / group["running_max"]
        - 1
    )
    
   
    max_dd = (
        group["drawdown"]
        .min()
    )
    trough_idx = (
        group["drawdown"]
        .idxmin()
    )

    trough_date = (
        group.loc[
            trough_idx,
            "date"
        ]
    )
    peak_nav = (
        group.loc[
            trough_idx,
            "running_max"
        ]
    )
    
    peak_date = (
        group[
            group["nav"] == peak_nav
        ]
        .iloc[0]["date"]
    )
    
    results.append({
        "amfi_code": amfi_code,
        "max_drawdown": max_dd,
        "peak_date": peak_date,
        "trough_date": trough_date
    })

drawdown_df = pd.DataFrame(
    results
)
drawdown_df.to_csv(
    "data/processed/fund_drawdowns.csv",
    index=False
)
    