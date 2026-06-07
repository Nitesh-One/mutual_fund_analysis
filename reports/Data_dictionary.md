# Data Dictionary

## Project: Mutual Fund Analytics Platform

---

# 1. Fund Master

**File:** `01_fund_master.csv`

**Purpose:** Stores master information for mutual fund schemes.

| Column             | Data Type | Business Definition                                |
| ------------------ | --------- | -------------------------------------------------- |
| amfi_code          | INTEGER   | Unique AMFI scheme identifier                      |
| fund_house         | TEXT      | Asset Management Company (AMC) managing the scheme |
| scheme_name        | TEXT      | Full scheme name                                   |
| category           | TEXT      | Fund category (Equity, Debt, Hybrid, etc.)         |
| sub_category       | TEXT      | Detailed SEBI sub-category                         |
| plan               | TEXT      | Direct or Regular plan                             |
| launch_date        | DATE      | Scheme launch date                                 |
| benchmark          | TEXT      | Benchmark index used for comparison                |
| expense_ratio_pct  | FLOAT     | Annual expense ratio (%) charged by the fund       |
| exit_load_pct      | FLOAT     | Exit load charged on redemption (%)                |
| min_sip_amount     | INTEGER   | Minimum SIP investment amount (₹)                  |
| min_lumpsum_amount | INTEGER   | Minimum lump-sum investment amount (₹)             |
| fund_manager       | TEXT      | Fund manager responsible for the scheme            |
| risk_category      | TEXT      | Risk classification of the scheme                  |
| sebi_category_code | TEXT      | SEBI category identifier                           |

---

# 2. NAV History

**File:** `02_nav_history.csv`

**Purpose:** Historical Net Asset Value records.

| Column    | Data Type | Business Definition      |
| --------- | --------- | ------------------------ |
| amfi_code | INTEGER   | Scheme identifier        |
| date      | DATE      | NAV valuation date       |
| nav       | FLOAT     | Net Asset Value per unit |

### Business Definition

NAV (Net Asset Value):

NAV = (Total Assets − Liabilities) ÷ Outstanding Units

---

# 3. AUM by Fund House

**File:** `03_aum_by_fund_house.csv`

**Purpose:** Fund house-level Assets Under Management statistics.

| Column         | Data Type | Business Definition                |
| -------------- | --------- | ---------------------------------- |
| date           | DATE      | Reporting date                     |
| fund_house     | TEXT      | AMC name                           |
| aum_lakh_crore | FLOAT     | AUM expressed in lakh crore rupees |
| aum_crore      | INTEGER   | AUM expressed in crore rupees      |
| num_schemes    | INTEGER   | Number of active schemes managed   |

### Business Definition

AUM (Assets Under Management) is the total market value of assets managed by a fund house.

---

# 4. Monthly SIP Inflows

**File:** `04_monthly_sip_inflows.csv`

**Purpose:** Industry-wide SIP trends.

| Column                    | Data Type | Business Definition                  |
| ------------------------- | --------- | ------------------------------------ |
| month                     | TEXT      | Reporting month (YYYY-MM)            |
| sip_inflow_crore          | INTEGER   | Monthly SIP inflow amount (₹ crore)  |
| active_sip_accounts_crore | FLOAT     | Active SIP accounts (crore)          |
| new_sip_accounts_lakh     | FLOAT     | Newly registered SIP accounts (lakh) |
| sip_aum_lakh_crore        | FLOAT     | SIP AUM (lakh crore)                 |
| yoy_growth_pct            | FLOAT     | Year-over-year growth percentage     |

---

# 5. Category Inflows

**File:** `05_category_inflows.csv`

**Purpose:** Category-level investment flows.

| Column           | Data Type | Business Definition                 |
| ---------------- | --------- | ----------------------------------- |
| month            | TEXT      | Reporting month                     |
| category         | TEXT      | Mutual fund category                |
| net_inflow_crore | FLOAT     | Net inflow/outflow amount (₹ crore) |

### Notes

* Positive values = net inflow
* Negative values = net outflow

---

# 6. Industry Folio Count

**File:** `06_industry_folio_count.csv`

**Purpose:** Tracks investor folio growth across fund categories.

| Column              | Data Type | Business Definition      |
| ------------------- | --------- | ------------------------ |
| month               | TEXT      | Reporting month          |
| total_folios_crore  | FLOAT     | Total mutual fund folios |
| equity_folios_crore | FLOAT     | Equity fund folios       |
| debt_folios_crore   | FLOAT     | Debt fund folios         |
| hybrid_folios_crore | FLOAT     | Hybrid fund folios       |
| others_folios_crore | FLOAT     | Other category folios    |

### Business Definition

A folio represents a unique investor account with an AMC.

---

# 7. Scheme Performance

**File:** `07_scheme_performance.csv`

**Purpose:** Performance and risk metrics of mutual fund schemes.

| Column             | Data Type | Business Definition                  |
| ------------------ | --------- | ------------------------------------ |
| amfi_code          | INTEGER   | Scheme identifier                    |
| scheme_name        | TEXT      | Scheme name                          |
| fund_house         | TEXT      | AMC name                             |
| category           | TEXT      | Fund category                        |
| plan               | TEXT      | Direct or Regular                    |
| return_1yr_pct     | FLOAT     | 1-year annualized return (%)         |
| return_3yr_pct     | FLOAT     | 3-year annualized return (%)         |
| return_5yr_pct     | FLOAT     | 5-year annualized return (%)         |
| benchmark_3yr_pct  | FLOAT     | Benchmark 3-year return (%)          |
| alpha              | FLOAT     | Excess return over benchmark         |
| beta               | FLOAT     | Volatility relative to benchmark     |
| sharpe_ratio       | FLOAT     | Risk-adjusted return metric          |
| sortino_ratio      | FLOAT     | Downside risk-adjusted return metric |
| std_dev_ann_pct    | FLOAT     | Annualized volatility (%)            |
| max_drawdown_pct   | FLOAT     | Maximum historical decline (%)       |
| aum_crore          | INTEGER   | Scheme AUM (₹ crore)                 |
| expense_ratio_pct  | FLOAT     | Expense ratio (%)                    |
| morningstar_rating | INTEGER   | Morningstar rating (1–5)             |
| risk_grade         | TEXT      | Risk level classification            |

---

# 8. Investor Transactions

**File:** `08_investor_transactions.csv`

**Purpose:** Individual investor transaction records.

| Column             | Data Type | Business Definition             |
| ------------------ | --------- | ------------------------------- |
| investor_id        | TEXT      | Unique investor identifier      |
| transaction_date   | DATE      | Transaction date                |
| amfi_code          | INTEGER   | Invested scheme identifier      |
| transaction_type   | TEXT      | SIP, Purchase, Redemption, etc. |
| amount_inr         | INTEGER   | Transaction amount in INR       |
| state              | TEXT      | Investor state                  |
| city               | TEXT      | Investor city                   |
| city_tier          | TEXT      | T30 or B30 classification       |
| age_group          | TEXT      | Investor age segment            |
| gender             | TEXT      | Investor gender                 |
| annual_income_lakh | FLOAT     | Annual income in lakh rupees    |
| payment_mode       | TEXT      | UPI, Net Banking, Cheque, etc.  |
| kyc_status         | TEXT      | KYC verification status         |

---

# 9. Portfolio Holdings

**File:** `09_portfolio_holdings.csv`

**Purpose:** Underlying securities held by mutual fund schemes.

| Column            | Data Type | Business Definition             |
| ----------------- | --------- | ------------------------------- |
| amfi_code         | INTEGER   | Scheme identifier               |
| stock_symbol      | TEXT      | NSE/BSE stock ticker            |
| stock_name        | TEXT      | Company name                    |
| sector            | TEXT      | Industry sector                 |
| weight_pct        | FLOAT     | Portfolio allocation percentage |
| market_value_cr   | FLOAT     | Holding market value (₹ crore)  |
| current_price_inr | FLOAT     | Current stock price             |
| portfolio_date    | DATE      | Portfolio disclosure date       |

---

# 10. Benchmark Indices

**File:** `10_benchmark_indices.csv`

**Purpose:** Historical benchmark index values.

| Column      | Data Type | Business Definition  |
| ----------- | --------- | -------------------- |
| date        | DATE      | Trading date         |
| index_name  | TEXT      | Benchmark index name |
| close_value | FLOAT     | Index closing value  |

Examples:

* NIFTY50
* NIFTY100 TRI
* SENSEX

---

# Key Relationships

### Primary Join Key

`amfi_code`

Used to connect:

* Fund Master
* NAV History
* Scheme Performance
* Investor Transactions
* Portfolio Holdings

### Time-Based Joins

`date`
`transaction_date`
`month`

Used for trend and time-series analysis.

---

# Data Quality Rules

1. `amfi_code` must be unique in Fund Master.
2. NAV values must be greater than zero.
3. AUM values cannot be negative.
4. Expense ratios cannot be negative.
5. Portfolio weights should not exceed 100% at scheme level.
6. Transaction amounts must be positive.
7. Benchmark values must be positive.
8. Missing AMFI codes should be rejected during ETL.

---

# Source System

Synthetic Mutual Fund Industry Dataset generated for Data Analytics, Data Engineering, SQL, and Power BI portfolio projects.

Last Updated: June 2026
