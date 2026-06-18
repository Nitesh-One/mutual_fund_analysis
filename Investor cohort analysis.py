import pandas as pd

df = pd.read_csv(
    "data/processed/cleaned_investor_transactions.csv"
)

df["transaction_date"] = pd.to_datetime(
    df["transaction_date"]
)

first_txn = (
    df.groupby("investor_id")
      ["transaction_date"]
      .min()
      .reset_index()
)

first_txn["cohort_year"] = (
    first_txn["transaction_date"]
    .dt.year
)

df = df.merge(
    first_txn[
        ["investor_id","cohort_year"]
    ],
    on="investor_id",
    how="left"
, validate="many_to_many")

avg_sip = (
    df[df["transaction_type"] == "SIP"]
    .groupby("cohort_year")
    ["amount_inr"]
    .mean()
    .reset_index(name="avg_sip_amount")
)

total_invested = (
    df.groupby("cohort_year")
    ["amount_inr"]
    .sum()
    .reset_index(name="total_invested")
)

top_fund = (
    df.groupby(
        ["cohort_year","transaction_type"]
    )
    .size()
    .reset_index(name="count")
)

top_fund = (
    top_fund.sort_values(
        ["cohort_year","count"],
        ascending=[True,False]
    )
    .groupby("cohort_year")
    .first()
    .reset_index()
)

top_fund = top_fund[
    ["cohort_year","transaction_type"]
].rename(
    columns={
        "transaction_type":"top_fund"
    }
)

cohort_analysis = (
    avg_sip
    .merge(total_invested,
           on="cohort_year")
    .merge(top_fund,
           on="cohort_year")
)

print(cohort_analysis)

cohort_analysis.to_csv(
    "data/processed/investor_cohort_analysis.csv",
    index=False
)
