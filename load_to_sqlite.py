"""Load processed mutual fund CSVs into a local SQLite database.

This module reads prepared CSV files and writes them into a SQLite
database used by the project.
"""

import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:///C:/Users/deepa/mutual_fund_analysis/mutual_fund.db"
)

# =========================
# READ FILES
# =========================

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/processed/cleaned_nav_history.csv")
transactions = pd.read_csv("data/processed/cleaned_investor_transactions.csv")
performance = pd.read_csv("data/processed/scheme_performance.csv")
aum = pd.read_csv("data/raw/03_aum_by_fund_house.csv")

# =========================
# DIM_FUND
# =========================

fund_master = fund_master[
    [
        "amfi_code",
        "scheme_name",
        "fund_house",
        "category",
        "sub_category",
        "plan",
        "risk_category"
    ]
]

fund_master.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

# =========================
# FACT_NAV
# =========================

nav_history = nav_history[
    [
        "amfi_code",
        "date",
        "nav"
    ]
]

nav_history.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

# =========================
# FACT_TRANSACTIONS
# =========================

transactions = transactions[
    [
        "investor_id",
        "transaction_date",
        "amfi_code",
        "transaction_type",
        "amount_inr",
        "state",
        "city",
        "city_tier",
        "age_group",
        "gender",
        "annual_income_lakh",
        "payment_mode",
        "kyc_status"
    ]
]

transactions.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

# =========================
# FACT_PERFORMANCE
# =========================

performance = performance[
    [
        "amfi_code",
        "scheme_name",
        "fund_house",
        "category",
        "plan",
        "return_1yr_pct",
        "return_3yr_pct",
        "return_5yr_pct",
        "benchmark_3yr_pct",
        "alpha",
        "beta",
        "sharpe_ratio",
        "sortino_ratio",
        "std_dev_ann_pct",
        "max_drawdown_pct",
        "aum_crore",
        "expense_ratio_pct",
        "morningstar_rating",
        "risk_grade"
    ]
]

performance.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

# =========================
# FACT_AUM
# =========================

aum = aum[
    [
        "date",
        "fund_house",
        "aum_lakh_crore",
        "aum_crore",
        "num_schemes"
    ]
]

aum.to_sql(
    "fact_aum",
    engine,
    if_exists="replace",
    index=False
)

# =========================
# VERIFY
# =========================

print(pd.read_sql("SELECT COUNT(*) FROM dim_fund", engine))
print(pd.read_sql("SELECT COUNT(*) FROM fact_nav", engine))
print(pd.read_sql("SELECT COUNT(*) FROM fact_transactions", engine))
print(pd.read_sql("SELECT COUNT(*) FROM fact_performance", engine))
print(pd.read_sql("SELECT COUNT(*) FROM fact_aum", engine))
