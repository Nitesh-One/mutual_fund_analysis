import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///mutual_fund.db")

print(pd.read_sql("SELECT COUNT(*) FROM dim_fund", engine))
print(pd.read_sql("SELECT COUNT(*) FROM fact_nav", engine))
print(pd.read_sql("SELECT COUNT(*) FROM fact_transactions", engine))
print(pd.read_sql("SELECT COUNT(*) FROM fact_performance", engine))
print(pd.read_sql("SELECT COUNT(*) FROM fact_aum", engine))