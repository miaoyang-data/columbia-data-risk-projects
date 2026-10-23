-- ====================================================================
-- Enterprise Risk Analytics & Data Extraction Queries
-- Author: Miao Yang
-- Description: SQL scripts for risk exposure aggregation, high-risk 
--              transaction anomaly detection, and portfolio VaR data extraction.
-- ====================================================================

-- 1. Aggregating Risk Exposure & Value at Risk (VaR) by Asset Class
SELECT 
    asset_class,
    COUNT(DISTINCT account_id) AS total_accounts,
    SUM(market_value) AS total_exposure_usd,
    AVG(volatility_30d) AS avg_volatility,
    PERCENTILE_CONT(0.05) WITHIN GROUP (ORDER BY daily_return) AS empirical_95_var
FROM portfolio_positions
WHERE position_date = CURRENT_DATE
GROUP BY asset_class
ORDER BY total_exposure_usd DESC;


-- 2. Fraud & Anomaly Detection: Identifying Suspicious Transactions
-- Flags accounts where daily transaction volume exceeds 3x user's historic average
WITH user_historical_stats AS (
    SELECT 
        account_id,
        AVG(transaction_amount) AS avg_tx_amount,
        STDDEV(transaction_amount) AS std_tx_amount
    FROM transaction_logs
    WHERE transaction_date >= CURRENT_DATE - INTERVAL '90 days'
    GROUP BY account_id
)
SELECT 
    t.transaction_id,
    t.account_id,
    t.transaction_amount,
    h.avg_tx_amount,
    (t.transaction_amount - h.avg_tx_amount) / NULLIF(h.std_tx_amount, 0) AS z_score_anomaly
FROM transaction_logs t
JOIN user_historical_stats h ON t.account_id = h.account_id
WHERE t.transaction_date = CURRENT_DATE
  AND (t.transaction_amount - h.avg_tx_amount) > (3 * h.std_tx_amount)
ORDER BY z_score_anomaly DESC;


-- 3. Extracting Historical Portfolio Returns for Python Risk Modeling
SELECT 
    p.portfolio_id,
    p.portfolio_name,
    d.trade_date,
    d.daily_return,
    d.portfolio_value
FROM portfolio_master p
JOIN daily_portfolio_performance d ON p.portfolio_id = d.portfolio_id
WHERE d.trade_date >= CURRENT_DATE - INTERVAL '1 year'
  AND p.status = 'ACTIVE';
