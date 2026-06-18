import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

returns = pd.read_csv(
    "data/processed/nav_daily_returns_corrected.csv"
)

returns["date"] = pd.to_datetime(
    returns["date"]
)
  
key_funds = [
    'SBI Bluechip Fund - Regular Plan - Growth',  
    'SBI Small Cap Fund - Regular Plan - Growth',      
    'SBI Magnum Gilt Fund - Regular Plan - Growth',        
    'HDFC Top 100 Fund - Regular Plan - Growth',                            
    'Nippon India Large Cap Fund - Regular - Growth'
]

rolling_results = []

plt.figure(figsize=(14,7))

for scheme_name in key_funds:

    fund = returns[
        returns["scheme"] == scheme_name
    ].copy()

    if fund.empty:
        print(f"{scheme_name} not found")
        continue

    fund = fund.sort_values("date")

    fund["rolling_sharpe"] = (
        fund["daily_return"]
        .rolling(90)
        .mean()
        /
        fund["daily_return"]
        .rolling(90)
        .std()
    ) * np.sqrt(252)

    rolling_results.append(fund)

    plt.plot(
        fund["date"],
        fund["rolling_sharpe"],
        label=scheme_name
    )

plt.xlabel("Date")
plt.ylabel("Sharpe Ratio")

plt.legend(loc="upper left")
plt.grid(True)

plt.tight_layout()

plt.show()

rolling_sharpe = pd.concat(
    rolling_results
)

rolling_sharpe.to_csv(
    "data/processed/rolling_sharpe_90d.csv",
    index=False
)
for scheme_name in key_funds:
    fund = returns[returns["scheme"] == scheme_name]
    print(scheme_name, len(fund))
# print(returns.columns.tolist())
  