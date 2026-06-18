import pandas as pd

df = pd.read_csv(
    "data/processed/cleaned_investor_transactions.csv"
)

df["transaction_date"] = pd.to_datetime(
    df["transaction_date"]
)

sip = df[
    df["transaction_type"] == "SIP"
].copy()

sip = sip.sort_values(
    ["investor_id", "transaction_date"]
)

sip["gap_days"] = (
    sip.groupby("investor_id")
       ["transaction_date"]
       .diff()
       .dt.days
)

eligible = (
    sip.groupby("investor_id")
       .size()
       .reset_index(name="sip_count")
)

eligible = eligible[
    eligible["sip_count"] >= 6
]

avg_gap = (
    sip.groupby("investor_id")
       ["gap_days"]
       .mean()
       .reset_index(name="avg_gap_days")
)

continuity = (
    eligible.merge(
        avg_gap,
        on="investor_id"
    )
)

continuity["status"] = (
    continuity["avg_gap_days"]
    .apply(
        lambda x:
        "At-Risk"
        if x > 35
        else "Active"
    )
)

continuity.to_csv(
    "data/processed/sip_continuity_analysis.csv",
    index=False
)

print(
    continuity.head()
)