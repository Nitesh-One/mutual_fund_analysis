import requests
import pandas as pd

url = "https://api.mfapi.in/mf/125497"

response = requests.get(url)

data = response.json()

# print(data.keys())

nav_df = pd.DataFrame(data["data"])

# print(nav_df)

nav_df.to_csv(
    "data/raw/hdfc_top100_direct_nav.csv",
    index=False
)

print(nav_df.head())

print(nav_df.shape)

schemes = {
    "sbi_bluechip": 119551,
    "icici_bluechip": 120503,
    "nippon_large_cap": 118632,
    "axis_bluechip": 119092,
    "kotak_bluechip": 120841
}

for fund_name, scheme_code in schemes.items():

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    response = requests.get(url)

    data = response.json()

    nav_df = pd.DataFrame(data["data"])

    nav_df.to_csv(
        f"data/raw/{fund_name}_nav.csv",
        index=False
    )

    print(f"Saved {fund_name}_nav.csv")




