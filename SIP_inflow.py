
import pandas as pd
import plotly.express as px

sip = pd.read_csv("data/raw/04_monthly_sip_inflows.csv")

sip["month"] = pd.to_datetime(sip["month"])


fig = px.line(
    sip,
    x="month",
    y="sip_inflow_crore",
    title="Monthly SIP Inflow Trend (Jan 2022 – Dec 2025)",
    markers=True,
)

fig.add_annotation(
    x="2025-12",
    y=31002,
    text="₹31,002 Cr All-Time High",
    showarrow=True,
    arrowhead=2,
)

fig.update_layout(
    hovermode="closest",
    xaxis_title="Month",
    yaxis_title="SIP Inflow (₹ Crore)",
    xaxis=dict(
        tickformat="%b %Y"
    ),
)

fig.show()
print(sip.columns)
