"""
Quantitative Risk Management & Statistical Analysis Toolkit
Columbia University - Enterprise Risk Management (ERM)
Author: Miao Yang

Description:
This script provides automated quantitative solutions for portfolio risk analytics,
hypothesis testing for mean bounds, Value at Risk (VaR), Expected Shortfall (ES),
and distribution-free risk estimation.
"""

import math
import numpy as np
from scipy import stats


def problem_1_mean_confidence():
    """
    Q1: One-sample t-test to determine confidence level that population mean > 40.
    Sample data: [64, 70, 20, 3, 58, 13, 74, 84, 47, 17]
    """
    data = np.array([64, 70, 20, 3, 58, 13, 74, 84, 47, 17])
    n = len(data)
    mean = np.mean(data)
    std_err = np.std(data, ddof=1) / math.sqrt(n)
    
    # Null Hypothesis H0: mu <= 40, Alternative H1: mu > 40
    t_stat = (mean - 40) / std_err
    p_value_one_tailed = 1 - stats.t.cdf(t_stat, df=n - 1)
    confidence_level = (1 - p_value_one_tailed) * 100

    print("=== Problem 1: Hypothesis Test for Mean > 40 ===")
    print(f"Sample Mean: {mean:.2f}")
    print(f"t-statistic: {t_stat:.4f}")
    print(f"Confidence Level (mean > 40): {confidence_level:.2f}%\n")
    return confidence_level


def problem_2_positive_return_confidence():
    """
    Q2: Probability/Confidence that portfolio manager continues to produce positive returns (> 0%).
    Sample returns: [-7%, 7%, 19%, 23%, -18%, -12%, 49%, 34%, -6%, -20%]
    """
    returns = np.array([-0.07, 0.07, 0.19, 0.23, -0.18, -0.12, 0.49, 0.34, -0.06, -0.20])
    n = len(returns)
    mean = np.mean(returns)
    std_err = np.std(returns, ddof=1) / math.sqrt(n)
    
    # Test if mean > 0
    t_stat = mean / std_err
    p_value = 1 - stats.t.cdf(t_stat, df=n - 1)
    confidence = (1 - p_value) * 100

    print("=== Problem 2: Portfolio Return Stability ===")
    print(f"Mean Annual Return: {mean * 100:.2f}%")
    print(f"Confidence for Positive Expected Returns: {confidence:.2f}%\n")
    return confidence


def problem_3_negative_return_prob():
    """
    Q3: Probability of negative return (Return < 0).
    Mean = 20%, Standard Deviation = 10%.
    1. Assuming Normal Distribution
    2. Assuming Symmetric Distribution (Cantelli's / Chebyshev's bound)
    """
    mu = 0.20
    sigma = 0.10
    
    # 1. Normal Distribution: P(X < 0) = P(Z < (0 - 0.20)/0.10) = P(Z < -2)
    z_score = (0 - mu) / sigma
    prob_normal = stats.norm.cdf(z_score)
    
    # 2. Symmetric unknown distribution: Gauss / Vysochanskij-Petunin or Cantelli's upper bound
    # Using Gauss Inequality for unimodal/symmetric: P(|X - mu| >= k*sigma) <= 4/(9*k^2)
    k = (mu - 0) / sigma  # k = 2
    prob_symmetric_bound = (1 / 2) * (1 / (1 + k**2)) # Cantelli / Selberg bound for one-tail

    print("=== Problem 3: Negative Return Probability ===")
    print(f"Normal Distribution Prob(Return < 0): {prob_normal * 100:.2f}%")
    print(f"Symmetrical Distribution Max Prob Upper Bound: {prob_symmetric_bound * 100:.2f}%\n")


def problem_4_uniform_distribution_var():
    """
    Q4: Uniform distribution between [-40%, +60%].
    Compute: Expected Return, 95% VaR, and Expected Shortfall (ES).
    """
    a = -0.40
    b = 0.60
    
    expected_return = (a + b) / 2
    
    # 95% VaR corresponds to 5th percentile of return distribution
    alpha = 0.05
    return_5pct = a + alpha * (b - a)  # -0.40 + 0.05 * 1.0 = -0.35
    var_95 = -return_5pct  # VaR expressed as loss positive number
    
    # Expected Shortfall = E[X | X <= return_5pct] = (-0.40 + -0.35) / 2 = -0.375
    expected_shortfall = -(a + return_5pct) / 2

    print("=== Problem 4: Uniform Distribution Risk Metrics ===")
    print(f"Expected Return: {expected_return * 100:.2f}%")
    print(f"95% Value at Risk (VaR): {var_95 * 100:.2f}%")
    print(f"95% Expected Shortfall (ES): {expected_shortfall * 100:.2f}%\n")


def problem_5_daily_portfolio_var():
    """
    Q5: Portfolio Daily Mean = 0.40%, Daily Std Dev = 2.30%.
    Assuming Normal Distribution. Compute 95% Daily VaR.
    """
    mu_daily = 0.0040
    sigma_daily = 0.0230
    
    # Z-score for 95% confidence (5th percentile) is ~ -1.6449
    z_95 = stats.norm.ppf(0.05)
    var_return = mu_daily + z_95 * sigma_daily
    var_95 = -var_return

    print("=== Problem 5: Portfolio Daily 95% VaR ===")
    print(f"95% Daily VaR (Loss %): {var_95 * 100:.2f}%")


if __name__ == "__main__":
    print("---------------------------------------------------------")
    print("  RUNNING QUANTITATIVE RISK & STATISTICAL ANALYTICS HUB  ")
    print("---------------------------------------------------------")
    problem_1_mean_confidence()
    problem_2_positive_return_confidence()
    problem_3_negative_return_prob()
    problem_4_uniform_distribution_var()
    problem_5_daily_portfolio_var()
