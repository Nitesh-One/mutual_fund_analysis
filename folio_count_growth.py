
import pandas as pd
import plotly.express as px

folio = pd.read_csv("data/raw/09_portfolio_holdings.csv")

folio["portfolio_date"] = pd.to_datetime(folio["portfolio_date"])

fig = px.line(
    folio,
    x="portfolio_date",
    y="market_value_cr",
    markers=True,
    title="Folio Count Growth (Jan 2022 - Dec 2025)"
)

# Starting milestone
fig.add_annotation(
    x="2022-01-01",
    y=13.26,
    text="13.26 Cr",
    showarrow=True
)

# Ending milestone
fig.add_annotation(
    x="2025-12-01",
    y=26.12,
    text="26.12 Cr",
    showarrow=True
)

fig.update_layout(
    hovermode="closest",
    xaxis_title="Month",
    yaxis_title="Folio Count (Cr)"
)

fig.update_traces(
    hovertemplate=
    "<b>%{x|%b %Y}</b><br>" +
    "Folios: %{y:.2f} Cr<extra></extra>"
)

fig.show()
