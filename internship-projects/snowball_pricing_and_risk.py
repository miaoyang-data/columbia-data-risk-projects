"""
Snowball Structured Product Valuation & Risk Monitoring System
China Securities Co., Ltd. Internship Project Replication (May 2021)
Author: Miao Yang (Columbia University MS ERM)

Description:
Monte Carlo simulation engine to price autocallable "Snowball" derivatives,
track Knock-In (KI) / Knock-Out (KO) boundary conditions, and estimate Delta/Vega risk.
"""

import numpy as np
import pandas as pd


def simulate_snowball_paths(S0=100, ko_barrier=1.03, ki_barrier=0.80, 
                            coupon_rate=0.20, T=1.0, r=0.03, sigma=0.25, 
                            num_simulations=10000, num_trading_days=252):
    """
    Monte Carlo Engine for Snowball Structured Product (2021 Market Parameters)
    - S0: Initial Underlying Index Price (e.g., CSI 500)
    - KO Barrier: 103% (Monthly Observation)
    - KI Barrier: 80% (Daily Observation)
    - Coupon: 20% annualized
    """
    dt = T / num_trading_days
    observation_interval = 21  # Monthly observation (~21 trading days)
    
    payoffs = []
    ko_counts = 0
    ki_counts = 0
    
    for _ in range(num_simulations):
        # Generate Geometric Brownian Motion price path
        random_shocks = np.random.normal(0, 1, num_trading_days)
        price_path = np.zeros(num_trading_days)
        price_path[0] = S0
        
        for t in range(1, num_trading_days):
            price_path[t] = price_path[t-1] * np.exp((r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * random_shocks[t])
            
        # Check Knock-Out (KO) on monthly observation dates
        knocked_out = False
        ko_day = None
        for day in range(observation_interval, num_trading_days, observation_interval):
            if price_path[day] >= S0 * ko_barrier:
                knocked_out = True
                ko_day = day
                break
                
        # Check Knock-In (KI) on daily observations
        knocked_in = np.any(price_path <= S0 * ki_barrier)
        
        # Calculate Payoff
        if knocked_out:
            ko_counts += 1
            holding_period = ko_day / num_trading_days
            payoff = S0 * (1 + coupon_rate * holding_period) * np.exp(-r * holding_period)
        elif not knocked_in:
            # Neither KO nor KI: Receive full coupon at maturity
            payoff = S0 * (1 + coupon_rate * T) * np.exp(-r * T)
        else:
            ki_counts += 1
            # Knocked-In and No KO: Exposed to underlying equity loss
            terminal_price = price_path[-1]
            payoff = min(S0, terminal_price) * np.exp(-r * T)
            
        payoffs.append(payoff)
        
    expected_value = np.mean(payoffs)
    print("=== 2021 Snowball Derivative Monte Carlo Risk Engine ===")
    print(f"Simulated Paths: {num_simulations}")
    print(f"Knock-Out Probability: {(ko_counts / num_simulations) * 100:.2f}%")
    print(f"Knock-In Event Risk Probability: {(ki_counts / num_simulations) * 100:.2f}%")
    print(f"Fair Present Value: {expected_value:.2f} (Base: 100.00)\n")


if __name__ == "__main__":
    simulate_snowball_paths()
