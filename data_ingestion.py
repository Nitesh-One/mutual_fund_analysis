from pathlib import Path
import pandas as pd

raw_path = Path("data/raw")

for file in raw_path.glob("*.csv"):
    df = pd.read_csv(file)

    print("=" * 60)
    print(f"Dataset: {file.name}")
    print("=" * 60)

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\n")
    
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
print("=" * 60)
print("Unique Fund house:")
print(fund_master["fund_house"].unique())
 
print("=" * 60)    
print("\nnumber of Fund house:")
print(fund_master["fund_house"].nunique())

print("=" * 60)    
print("\nUnique Categories:")
print(fund_master["category"].unique())

print("=" * 60)    
print("\nUnique Risk Grades:")
print(fund_master["risk_category"].unique())

print("=" * 60)
print(fund_master["amfi_code"].head())
print(fund_master["amfi_code"].dtype)

print("\nNumber of unique AMFI codes:")
print(fund_master["amfi_code"].nunique())

print("\nTotal rows:")
print(len(fund_master))


nav_history = pd.read_csv("data/raw/02_nav_history.csv")
print("=" * 60)
print(fund_master.columns.tolist())
print(nav_history.columns.tolist())

fund_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing_codes = fund_codes - nav_codes
print(f"\nMissing AMFI codes in NAV history: {len(missing_codes)}")

print("Fund Master Codes:", len(fund_codes))
print("NAV History Codes:", len(nav_codes))

if len(missing_codes) == 0:
    print("All AMFI codes exist in nav_history.")
else:
    print("Missing codes:")
    print(missing_codes)
    
duplicates = fund_master["amfi_code"].duplicated().sum()
print("Duplicate AMFI codes:", duplicates)    

print(fund_master.isnull().sum())

