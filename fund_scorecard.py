import pandas as pd

cagr = pd.read_csv(
    "data/processed/fund_cagr_comparison.csv"
)

sharpe = pd.read_csv(
    "data/processed/fund_sharpe_ranking.csv"
)

alpha = pd.read_csv(
    "data/processed/fund_alpha_beta.csv"
)

drawdown = pd.read_csv(
    "data/processed/fund_drawdowns.csv"
)

expense = pd.read_csv(
    "data/processed/scheme_performance.csv"
)

scorecard = (
    cagr[["amfi_code", "cagr_3y"]]
    .merge(
        sharpe[["amfi_code", "sharpe_ratio"]],
        on="amfi_code"
    )
    .merge(
        alpha[["amfi_code", "alpha"]],
        on="amfi_code"
    )
    .merge(
        drawdown[
            ["amfi_code", "max_drawdown"]
        ],
        on="amfi_code"
    )
    .merge(
        expense[
            ["amfi_code", "expense_ratio_pct"]
        ],
        on="amfi_code"
    )
)

scorecard["return_rank"] = (
    scorecard["cagr_3y"]
    .rank(ascending=False)
)

scorecard["sharpe_rank"] = (
    scorecard["sharpe_ratio"]
    .rank(ascending=False)
)

scorecard["alpha_rank"] = (
    scorecard["alpha"]
    .rank(ascending=False)
)

scorecard["expense_rank"] = (
    scorecard["expense_ratio_pct"]
    .rank(ascending=True)
)

scorecard["dd_rank"] = (
    scorecard["max_drawdown"]
    .rank(ascending=False)
)

n = len(scorecard)

scorecard["return_score"] = (
    (n - scorecard["return_rank"])
    / (n - 1)
) * 100

scorecard["sharpe_score"] = (
    (n - scorecard["sharpe_rank"])
    / (n - 1)
) * 100

scorecard["alpha_score"] = (
    (n - scorecard["alpha_rank"])
    / (n - 1)
) * 100

scorecard["expense_score"] = (
    (n - scorecard["expense_rank"])
    / (n - 1)
) * 100

scorecard["dd_score"] = (
    (n - scorecard["dd_rank"])
    / (n - 1)
) * 100

scorecard["fund_score"] = (

    0.30
    * scorecard["return_score"]

    +

    0.25
    * scorecard["sharpe_score"]

    +

    0.20
    * scorecard["alpha_score"]

    +

    0.15
    * scorecard["expense_score"]

    +

    0.10
    * scorecard["dd_score"]

)

scorecard = scorecard.sort_values(
    by="fund_score",
    ascending=False
)

scorecard["overall_rank"] = (
    range(
        1,
        len(scorecard) + 1
    )
)

scorecard.to_csv(
    "data/processed/fund_scorecard.csv",
    index=False
)
