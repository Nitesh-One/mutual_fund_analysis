import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


aum = pd.read_csv("data/raw/03_aum_by_fund_house.csv")

aum["date"] = pd.to_datetime(aum["date"])
aum["year"] = aum["date"].dt.year

# Keep only 2022–2025
aum = aum[
    (aum["year"] >= 2022) &
    (aum["year"] <= 2025)
]

plt.figure(figsize=(14, 7))

sns.barplot(
    data=aum,
    x="year",
    y="aum_crore",
    hue="fund_house"
)

plt.title("AUM Growth by Fund House (2022–2025)")
plt.xlabel("Year")
plt.ylabel("AUM (₹ Crore)")
plt.grid(True)

plt.xticks(rotation=0)

plt.annotate(
    "SBI ₹12.5L Cr",
    xy=(3, 1250000),
    xytext=(2.5, 1350000),
    arrowprops={"arrowstyle": "->"}
)

plt.tight_layout()
plt.show()
