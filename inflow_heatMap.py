import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data/raw/05_category_inflows.csv")

df["month"] = pd.to_datetime(df["month"])

df["month"] = df["month"].dt.strftime("%b")

heatmap_data = df.pivot_table(
    index="category",
    columns="month",
    values="net_inflow_crore",
    aggfunc="sum"
)

month_order = [
    "Jan","Feb","Mar","Apr",
    "May","Jun","Jul","Aug",
    "Sep","Oct","Nov","Dec"
]

heatmap_data = heatmap_data.reindex(
    columns=month_order
)

plt.figure(figsize=(12, 6))

sns.heatmap(
    heatmap_data,
    annot=True,
    fmt=".0f",
    cmap="YlGnBu",
     linewidths=0.5,
     cbar = True,
)

plt.title("Category Net Inflow Heatmap")
plt.xlabel("Month")
plt.ylabel("Fund Category")

plt.tight_layout()
plt.show()
# print(df.columns)
