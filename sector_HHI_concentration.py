import pandas as pd

sector = pd.read_csv(
    "data/processed/sector_allocation.csv"
)

sector["weight"] = (
    sector["weight_pct"] / 100
)

sector["weight_sq"] = (
    sector["weight"] ** 2
)

hhi = (
    sector.groupby(
        ["amfi_code","scheme_name"]
    )["weight_sq"]
    .sum()
    .reset_index()
)

hhi.rename(
    columns={
        "weight_sq":"hhi"
    },
    inplace=True
)

def classify_hhi(x):

    if x < 0.15:
        return "Diversified"

    elif x < 0.25:
        return "Moderate"

    else:
        return "Concentrated"


hhi["concentration"] = (
    hhi["hhi"]
    .apply(classify_hhi)
)

hhi = hhi.sort_values(
    "hhi",
    ascending=False
)

print(hhi.head(10))

hhi.to_csv(
    "data/processed/fund_sector_hhi.csv",
    index=False
)
