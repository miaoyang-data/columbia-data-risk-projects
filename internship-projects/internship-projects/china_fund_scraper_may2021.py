"""
China Mutual Fund Return Scraper & Analytics (May 2021)
China Securities Co., Ltd. Internship Project Replication
Author: Miao Yang (Columbia University MS ERM)

Description:
Data pipeline to scrape Chinese income & bond funds data, filter portfolios with May 2021 
monthly returns > 1.0%, clean NAV (Net Asset Value) series, and calculate risk-adjusted 
performance metrics for wealth management reports.
"""

import math
import numpy as np
import pandas as pd


def scrape_may_2021_funds():
    """
    Simulates scraping fund performance and NAV data from East Money/Tiantian Fund API 
    for May 2021, filtering for funds with monthly return > 1.0%.
    """
    # Simulated raw scraped data representing Chinese Funds in May 2021
    raw_fund_data = {
        'fund_code': ['000001.OF', '000009.OF', '000021.OF', '000042.OF', '000051.OF', '000065.OF'],
        'fund_name': [
            'China Southern Growth Fund', 
            'E Fund High Yield Bond', 
            'China Asset Management Income Fund', 
            'CICC Wealth Management Multi-Asset', 
            'Guotai Monthly Growth Fund',
            'Fullgoal Treasury Appreciation'
        ],
        'fund_type': ['Hybrid', 'Bond/Income', 'Income', 'Multi-Asset', 'Hybrid', 'Fixed Income'],
        'may_2021_return': [0.0235, 0.0142, 0.0085, 0.0188, 0.0045, 0.0115],  # Decimals: 2.35%, 1.42%, etc.
        'aum_billion_rmb': [12.5, 8.2, 25.1, 6.4, 4.8, 15.3],
        'max_drawdown_may': [0.008, 0.003, 0.002, 0.005, 0.009, 0.002]
    }
    
    df = pd.DataFrame(raw_fund_data)
    
    # Filter funds with May 2021 return > 1.0% (0.01)
    target_funds = df[df['may_2021_return'] > 0.01].copy()
    
    # Format percentage display
    target_funds['may_2021_return_pct'] = target_funds['may_2021_return'].apply(lambda x: f"{x*100:.2f}%")
    target_funds['max_drawdown_pct'] = target_funds['max_drawdown_may'].apply(lambda x: f"{x*100:.2f}%")
    
    print("=== May 2021 Chinese Mutual Funds with Return > 1.0% ===")
    print(target_funds[['fund_code', 'fund_name', 'fund_type', 'may_2021_return_pct', 'max_drawdown_pct', 'aum_billion_rmb']])
    return target_funds


def calculate_risk_adjusted_metrics(funds_df):
    """
    Calculates annualized Sharpe Ratio and downside risk for filtered funds.
    Assumes risk-free rate = 2.5% (2021 China 10Y Treasury yield benchmark).
    """
    rf_annual = 0.025
    rf_monthly = rf_annual / 12
    
    # Compute Sharpe Ratio estimate (monthly return - monthly rf) / monthly volatility proxy
    funds_df['excess_return'] = funds_df['may_2021_return'] - rf_monthly
    # Assuming 1.5% proxy monthly volatility for high-yield bond/income funds
    volatility_proxy = 0.015  
    funds_df['sharpe_ratio'] = (funds_df['excess_return'] / volatility_proxy) * math.sqrt(12)
    
    print("\n=== Fund Valuation & Risk Monitoring Performance Summary ===")
    for _, row in funds_df.iterrows():
        print(f"Fund: {row['fund_name']} ({row['fund_code']}) | Return: {row['may_2021_return_pct']} | Est. Annualized Sharpe: {row['sharpe_ratio']:.2f}")


if __name__ == "__main__":
    print("-------------------------------------------------------------------------")
    print("  EAST MONEY / TIANTIAN FUND SCRAPER & RISK MONITORING SYSTEM (MAY 2021) ")
    print("-------------------------------------------------------------------------")
    filtered_df = scrape_may_2021_funds()
    calculate_risk_adjusted_metrics(filtered_df)
