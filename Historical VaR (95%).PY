import pandas as pd

returns = pd.read_csv(
    "data/processed/nav_daily_returns.csv"
)

results = []

for amfi_code, group in returns.groupby(
    "amfi_code"
):

    var_95 = group[
        "daily_return"
    ].quantile(0.05)

    cvar_95 = group.loc[
        group["daily_return"] <= var_95,
        "daily_return"
    ].mean()

    results.append({
        "amfi_code": amfi_code,
        "var_95": var_95,
        "cvar_95": cvar_95
    })

risk_metrics = pd.DataFrame(
    results
)

risk_metrics.to_csv(
    "data/processed/fund_var_cvar.csv",
    index=False
)

print(
    risk_metrics.head()
)