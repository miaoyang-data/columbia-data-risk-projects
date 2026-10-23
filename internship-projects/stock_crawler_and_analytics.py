"""
East Money Stock Scraper & Fund Risk Analytics Pipeline
China Securities Co., Ltd. Internship Project Replication
Author: Miao Yang (Columbia University MS ERM)

Description:
Automated data pipeline to scrape A-share market performance data (March 2021),
filter equities with monthly returns > 5%, clean raw financial datasets using Pandas,
and generate valuation & risk monitoring metrics for income fund portfolios.
"""

import math
import numpy as np
import pandas as pd


def scrape_and_filter_stocks():
    """
    Simulates scraping market performance data (East Money standard format)
    and filters stocks with March 2021 return > 5%.
    """
    # Simulated raw scraped dataset from East Money (March 2021)
    raw_data = {
        'ticker': ['600519.SH', '000858.SZ', '601318.SH', '000001.SZ', '600036.SH', '300750.SZ'],
        'stock_name': ['Kweichow Moutai', 'Wuliangye', 'Ping An Insurance', 'Ping An Bank', 'CM Bank', 'CATL'],
        'sector': ['Consumer', 'Consumer', 'Financials', 'Financials', 'Financials', 'Clean Energy'],
        'march_2021_return': [0.065, 0.082, -0.021, 0.054, 0.071, -0.045],  # 6.5%, 8.2%, -2.1%, 5.4%, 7.1%, -4.5%
        'market_cap_bn': [2600.5, 1100.2, 1400.8, 420.5, 1250.3, 850.6],
        'pe_ratio': [45.2, 38.5, 10.2, 11.5, 12.8, 115.0]
    }
    
    df = pd.DataFrame(raw_data)
    
    # Filter equities with monthly gain > 5%
    filtered_df = df[df['march_2021_return'] > 0.05].copy()
    filtered_df['march_2021_return_pct'] = filtered_df['march_2021_return'].apply(lambda x: f"{x*100:.2f}%")
    
    print("=== March 2021 A-Share Equities with Gain > 5% ===")
    print(filtered_df[['ticker', 'stock_name', 'sector', 'march_2021_return_pct', 'pe_ratio']])
    return filtered_df


def fund_risk_monitoring_pipeline(stocks_df):
    """
    Data analytics pipeline for fund performance valuation and risk monitoring.
    Calculates portfolio weighted return, downside risk, and concentration metrics.
    """
    # Portfolio allocation weights for filtered outperforming stocks
    weights = np.array([0.35, 0.25, 0.20, 0.20])
    returns = stocks_df['march_2021_return'].values
    
    # Portfolio Return & Risk Metrics
    portfolio_return = np.dot(weights, returns)
    portfolio_volatility = np.std(returns) * math.sqrt(12)  # Annualized volatility proxy
    max_drawdown_estimate = np.min(returns) - np.mean(returns)
    
    print("\n=== Income Fund Valuation & Risk Monitoring Output ===")
    print(f"Weighted Portfolio March Return: {portfolio_return * 100:.2f}%")
    print(f"Portfolio Annualized Volatility: {portfolio_volatility * 100:.2f}%")
    print(f"Downside Risk Exposure Estimate: {max_drawdown_estimate * 100:.2f}%")


if __name__ == "__main__":
    print("------------------------------------------------------------------")
    print("  EAST MONEY DATA PIPELINE & FUND RISK MONITORING SYSTEM  ")
    print("------------------------------------------------------------------")
    outperforming_stocks = scrape_and_filter_stocks()
    fund_risk_monitoring_pipeline(outperforming_stocks)
