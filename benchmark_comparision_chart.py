import pandas as pd
import plotly.express as px
import numpy as np

scorecard = pd.read_csv(
    "data/processed/fund_scorecard.csv"
)

nav = pd.read_csv(
    "data/processed/cleaned_nav_history.csv"
)

benchmark = pd.read_csv(
    "data/raw/10_benchmark_indices.csv"
)

fund = pd.read_csv(
    "data/processed/nav_daily_returns.csv"
)

fund["date"] = pd.to_datetime(
    fund["date"]
)

nav["date"] = pd.to_datetime(
    nav["date"]
)

benchmark["date"] = pd.to_datetime(
    benchmark["date"]
)

top5 = (
    scorecard
    .sort_values(
        "fund_score",
        ascending=False
    )
    .head(5)
)

top5_codes = top5["amfi_code"].tolist()

nav = nav[
    nav["amfi_code"].isin(top5_codes)
]

nav["normalized_nav"] = (
    nav.groupby("amfi_code")["nav"]
       .transform(
           lambda x:
           x / x.iloc[0] * 100
       )
)

benchmark = benchmark[
    benchmark["index_name"]
    .isin(
        ["NIFTY50", "NIFTY100"]
    )
]

benchmark["normalized"] = (
    benchmark.groupby("index_name")
             ["close_value"]
             .transform(
                 lambda x:
                 x / x.iloc[0] * 100
             )
)


fig = px.line()

for fund_id, grp in nav.groupby(
    "amfi_code"
):
    fig.add_scatter(
        x=grp["date"],
        y=grp["normalized_nav"],
        mode="lines",
        name=str(fund_id)
    )

for benchmark_name, grp in benchmark.groupby(
    "index_name"
):
    fig.add_scatter(
        x=grp["date"],
        y=grp["normalized"],
        mode="lines",
        name=benchmark_name
    )

fig.update_layout(
    title=
    "Top 5 Funds vs Nifty 50 & Nifty 100",
    yaxis_title=
    "Normalized Growth (Base=100)"
)

fig.show()

nifty100 = benchmark[
    benchmark["index_name"]
    == "NIFTY100"
].copy()

nifty100["benchmark_return"] = (
    nifty100["close_value"]
    .pct_change()
)


tracking_results = []

for amfi_code, group in fund.groupby(
    "amfi_code"
):
    merged = pd.merge(
      group,
      nifty100[
          [
            "date",
            "benchmark_return"
         ]
        ],
      on="date",
      how="inner",
      validate="many_to_one"
    )

    merged["active_return"] = (
        merged["daily_return"]
        -
        merged["benchmark_return"]
    )
    
    tracking_error = (
        merged["active_return"]
        .std()
        *
        np.sqrt(252)
    )
    tracking_results.append({
        "amfi_code": amfi_code,
        "tracking_error":
            tracking_error
    })
    
tracking_df = pd.DataFrame(
    tracking_results
)

tracking_df.to_csv(
    "data/processed/tracking_error.csv",
    index=False
)
    