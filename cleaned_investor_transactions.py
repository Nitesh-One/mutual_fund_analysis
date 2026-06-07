import pandas as pd
investor_transactions = pd.read_csv('data/raw/08_investor_transactions.csv')

# print(investor_transactions.columns)

# print(investor_transactions['transaction_type'].unique())

investor_transactions['transaction_type'] = (investor_transactions["transaction_type"].str.strip().str.lower())

# print(investor_transactions['transaction_type'].unique())

investor_transactions["transaction_type"] = (
    investor_transactions["transaction_type"]
    .replace({
        "sip": "SIP",
        "lump sum": "Lumpsum",
        "lumpsum": "Lumpsum",
        "redeem": "Redemption",
        "redemption": "Redemption"
    })
)
print(investor_transactions["transaction_type"].unique())

invalid_amounts = investor_transactions[investor_transactions['amount_inr'] <= 0]

print(invalid_amounts)
print(
    "Invalid Amount Records:",
    len(invalid_amounts)
)

transactions = investor_transactions[
    investor_transactions["amount_inr"] > 0
]

investor_transactions['transaction_date'] = pd.to_datetime(investor_transactions['transaction_date'])

# print(investor_transactions["transaction_date"].dtype)

print(investor_transactions['kyc_status'].unique())

valid_kyc = {
    "Verified",
    "Pending",
}

invalid_kyc = investor_transactions[
    ~investor_transactions["kyc_status"]
    .isin(valid_kyc)
]

# print(invalid_kyc)

transactions[
    ~transactions["kyc_status"].isin(valid_kyc)
]
investor_transactions.to_csv("data/processed/cleaned_investor_transactions.csv", index=False)