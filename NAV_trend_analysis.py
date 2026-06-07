
"""NAV trend analysis plotting for mutual fund schemes.

This module loads cleaned NAV history and plots NAV trends with
highlighted periods. The module-level name is preserved for
backwards compatibility; disable the naming lint warning.
"""

# Disable naming-style warning for module filename
# pylint: disable=invalid-name

import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("data/processed/cleaned_nav_history.csv")

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Plot all schemes
fig = px.line(
    df,
    x="date",
    y="nav",
    color="amfi_code",
    title="NAV Trend Analysis (2022-2026)"
)

# Highlight 2023 Bull Run
fig.add_vrect(
    x0="2023-01-01",
    x1="2023-12-31",
    annotation_text="2023 Bull Run",
    fillcolor="green",
    opacity=0.15,
    line_width=0
)

# Highlight 2024 Market Corrections
fig.add_vrect(
    x0="2024-01-01",
    x1="2024-12-31",
    annotation_text="2024 Correction",
    fillcolor="red",
    opacity=0.15,
    line_width=0
)

fig.update_layout(
    xaxis_title="Date",
    yaxis_title="NAV",
    hovermode="closest"    
)

fig.show()
