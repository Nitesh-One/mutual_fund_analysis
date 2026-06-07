import pandas as pd

scheme_performance = pd.read_csv('data/raw/07_scheme_performance.csv')

print(scheme_performance.columns)
print(scheme_performance.head())

return_cols = ["return_1yr_pct", "return_3yr_pct", "return_5yr_pct"]

for col in return_cols:
    scheme_performance[col] = pd.to_numeric(scheme_performance[col], errors='coerce')
    
for col in return_cols:
    invalid_returns = scheme_performance[
        scheme_performance[col].isnull()
    ]

    print(f"\nInvalid values in {col}:")
    print(len(invalid_returns))

for col in return_cols:

    anomalies = scheme_performance[
        (scheme_performance[col] < -100)
        |
        (scheme_performance[col] > 100)
    ]

    print(f"\nAnomalies in {col}:")
    print(anomalies)

invalid_expense_ratio = scheme_performance[
    (scheme_performance["expense_ratio_pct"] < 0.1)
    |
    (scheme_performance["expense_ratio_pct"] > 2.5)
]

print(invalid_expense_ratio)
print(
    "Invalid Expense Ratios:",
    len(invalid_expense_ratio)
)

scheme_performance.to_csv(
    "data/processed/scheme_performance.csv",
    index=False
)           