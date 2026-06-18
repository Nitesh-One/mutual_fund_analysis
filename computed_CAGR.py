import pandas as pd

nav = pd.read_csv(
    "data/processed/cleaned_nav_history.csv"
)

nav["date"] = pd.to_datetime(nav["date"])

nav = nav.sort_values(
    ["amfi_code", "date"]
)

def calculate_cagr(nav_start, nav_end, years):

    if nav_start <= 0:
        return None

    return (
        (nav_end / nav_start) ** (1 / years)
    ) - 1
    
results = []

for amfi_code, group in nav.groupby("amfi_code"):

    group = group.sort_values("date")

    nav_end_value = group.iloc[-1]["nav"]

    cagr_1y = None
    cagr_3y = None
    cagr_5y = None
    
    date_1y = (
        group.iloc[-1]["date"]
        - pd.DateOffset(years=1)
    )

    start_1y = group[
        group["date"] >= date_1y
    ].iloc[0]["nav"]

    cagr_1y = calculate_cagr(
        start_1y,
        nav_end_value,
        1
    )
    
    date_3y = (
        group.iloc[-1]["date"]
        - pd.DateOffset(years=3)
    )

    start_3y = group[
        group["date"] >= date_3y
    ].iloc[0]["nav"]

    cagr_3y = calculate_cagr(
        start_3y,
        nav_end_value,
        3
    )
    
    date_5y = (
        group.iloc[-1]["date"]
        - pd.DateOffset(years=5)
    )

    start_5y = group[
        group["date"] >= date_5y
    ].iloc[0]["nav"]

    cagr_5y = calculate_cagr(
        start_5y,
        nav_end_value,
        5
    )
    
    results.append({
        "amfi_code": amfi_code,
        "cagr_1y": cagr_1y,
        "cagr_3y": cagr_3y,
        "cagr_5y": cagr_5y
    })
    
cagr_df = pd.DataFrame(results)    

cagr_df["cagr_1y"] *= 100
cagr_df["cagr_3y"] *= 100
cagr_df["cagr_5y"] *= 100

cagr_df = cagr_df.round(2)

print(cagr_df.head())

cagr_df.to_csv(
    "data/processed/fund_cagr_comparison.csv",
    index=False
)
