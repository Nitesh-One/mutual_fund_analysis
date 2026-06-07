-- #1
SELECT
    fund_house,
    aum_crore
FROM fact_aum
ORDER BY aum_crore DESC
LIMIT 5;

-- #2
SELECT
    strftime('%Y', date) AS year,
    strftime('%m', date) AS month,
    ROUND(AVG(nav), 2) AS avg_nav
FROM fact_nav
GROUP BY year, month
ORDER BY year, month;
-- #3
SELECT
    strftime('%Y', transaction_date) AS year,
    SUM(amount_inr) AS sip_amount
FROM fact_transactions
WHERE transaction_type = 'SIP'
GROUP BY year
ORDER BY year;

-- #4
SELECT
    state,
    COUNT(*) AS transaction_count,
    SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;

-- #5
SELECT
    scheme_name,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- #6
SELECT
    scheme_name,
    return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;

-- #7
SELECT
    category,
    ROUND(AVG(expense_ratio_pct), 2) AS avg_expense_ratio
FROM fact_performance
GROUP BY category;
-- #8
SELECT
    transaction_type,
    SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY transaction_type;

-- #9
SELECT
    fund_house,
    COUNT(*) AS scheme_count
FROM dim_fund
GROUP BY fund_house
ORDER BY scheme_count DESC;

-- #10
SELECT
    fund_house,
    aum_crore
FROM fact_aum
ORDER BY aum_crore DESC
LIMIT 5;

-- SELECT COUNT(*) FROM dim_fund;
-- SELECT COUNT(*) FROM fact_nav;
-- SELECT COUNT(*) FROM fact_transactions;
-- SELECT COUNT(*) FROM fact_performance;
-- SELECT COUNT(*) FROM fact_aum;

-- SELECT * FROM dim_fund LIMIT 5;
-- SELECT * FROM fact_nav LIMIT 5;
-- SELECT * FROM dim_fund LIMIT 5;
-- SELECT fund_id, amfi_code
-- FROM dim_fund
-- LIMIT 5;
-- SELECT *
-- FROM fact_nav
-- LIMIT 5;

