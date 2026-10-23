"""
CSCEC Group HQ - 135+ Subsidiaries Liquidity & Capital Allocation Model
China State Construction Engineering Corporation (CSCEC Group) Project Replication
Author: Miao Yang (Columbia University MS ERM)

Description:
Multi-dimensional risk monitoring framework evaluating:
1. Liquidity Risk: Cash-to-Short-Term Debt Ratio & Quick Ratio.
2. Capital Allocation Efficiency: ROIC (Return on Invested Capital) vs. WACC spread.
3. Long-Term Project Viability: NPV, IRR, and Cash Flow Stress Testing across 135+ subsidiaries.
"""

import numpy as np
import pandas as pd


def generate_135_subsidiaries_data():
    """
    Simulates financial and liquidity datasets across 135+ CSCEC subsidiaries.
    """
    np.random.seed(42)
    n_subs = 135
    
    sub_ids = [f"CSCEC-SUB-{i:03d}" for i in range(1, n_subs + 1)]
    sectors = np.random.choice(['Infrastructure', 'Building Construction', 'Real Estate', 'Overseas Engineering', 'Design & Survey'], n_subs)
    
    # Financial metrics generation
    cash_and_equivalents_m = np.random.uniform(50, 2000, n_subs)  # RMB Millions
    st_debt_m = np.random.uniform(30, 1500, n_subs)
    current_assets_m = cash_and_equivalents_m + np.random.uniform(100, 3000, n_subs)
    current_liab_m = st_debt_m + np.random.uniform(50, 1000, n_subs)
    
    roic = np.random.normal(0.065, 0.025, n_subs)  # Avg ROIC 6.5%
    wacc = np.random.uniform(0.040, 0.055, n_subs) # Cost of Capital 4.0% - 5.5%
    
    # Project viability parameters
    project_npv_m = np.random.normal(120, 80, n_subs)
    project_irr = roic + np.random.normal(0.02, 0.01, n_subs)
    
    df = pd.DataFrame({
        'subsidiary_id': sub_ids,
        'sector': sectors,
        'cash_m': cash_and_equivalents_m,
        'st_debt_m': st_debt_m,
        'current_assets_m': current_assets_m,
        'current_liab_m': current_liab_m,
        'roic': roic,
        'wacc': wacc,
        'project_npv_m': project_npv_m,
        'project_irr': project_irr
    })
    return df


def evaluate_liquidity_and_viability(df):
    """
    Evaluates multi-dimensional risk metrics for corporate treasury & risk oversight.
    """
    # 1. Liquidity Indicators
    df['cash_to_st_debt'] = df['cash_m'] / df['st_debt_m']
    df['quick_ratio'] = df['cash_m'] / df['current_liab_m']
    df['liquidity_warning'] = df['cash_to_st_debt'] < 1.0  # Cash coverage warning
    
    # 2. Capital Allocation Efficiency (EVA / Spread)
    df['capital_spread'] = df['roic'] - df['wacc']
    df['capital_efficiency'] = np.where(df['capital_spread'] > 0.015, 'High Value Add',
                               np.where(df['capital_spread'] > 0, 'Value Neutral', 'Capital Destructive'))
    
    # 3. Long-Term Project Viability Score
    # Score based on Positive NPV and IRR > WACC threshold
    df['project_viability'] = (df['project_npv_m'] > 0) & (df['project_irr'] > df['wacc'] + 0.02)
    
    # Summary Risk Classification
    high_risk_subs = df[(df['liquidity_warning']) | (df['capital_efficiency'] == 'Capital Destructive')]
    
    print("=== CSCEC HQ Group Risk Oversight Summary (135 Subsidiaries) ===")
    print(f"Total Subsidiaries Monitored: {len(df)}")
    print(f"Subsidiaries with Liquidity Warnings: {df['liquidity_warning'].sum()}")
    print(f"Capital Destructive Entities (ROIC < WACC): {(df['capital_efficiency'] == 'Capital Destructive').sum()}")
    print(f"Subsidiaries with High Long-Term Project Viability: {df['project_viability'].sum()}\n")
    
    print("=== Sample High Risk Subsidiaries Requiring Intervention ===")
    print(high_risk_subs[['subsidiary_id', 'sector', 'cash_to_st_debt', 'capital_spread', 'project_viability']].head())
    
    return df


if __name__ == "__main__":
    print("-------------------------------------------------------------------------")
    print("  CSCEC GROUP HQ - TREASURY & RISK MONITORING ENGINE (135+ SUBSIDIARIES) ")
    print("-------------------------------------------------------------------------")
    raw_data = generate_135_subsidiaries_data()
    evaluated_df = evaluate_liquidity_and_viability(raw_data)
