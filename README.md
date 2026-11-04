# Columbia Quantitative Risk Analytics & Asset-Backed Modeling

This repository contains modular quantitative risk pipelines, data processing frameworks, and risk-management toolkits developed by **Miao Yang** (M.S. in Enterprise Risk Management, Columbia University). 

The frameworks focus on **Credit Risk Scoring, Value at Risk (VaR) Engine, Scenario Stress Testing, and Structured Asset Cash-Flow Modeling**, with direct applications in emerging alternative asset financing (e.g., Robotics & Hardware-as-a-Service).

---

## 🛠️ Repository Architecture & Module Overview

### 1. Robotics Asset Financing & Credit Guardrails (Featured Demo)
* **`robotics_cashflow_var_demo.py`**: A specialized risk engine designed for **Robotics-as-a-Service (RaaS) credit underwriting**. 
  * **Core Logic**: Models asset-generated revenues tied to **human labor cost savings**, incorporates **end-market industry cyclicality shocks**, and runs Monte Carlo simulations to calculate 95% Portfolio Value at Risk (VaR) and debt-underwriting guardrails.

### 2. Credit Risk Scoring & Data Extraction Pipeline
* **`cscec_subsidiary_risk_model.py`**: Multi-dimensional liquidity and cash flow waterfall stress-testing model evaluating debt coverage, capital allocation efficiency, and project viability scores across B2B entities.
* **`risk_data_queries.sql`**: Production SQL scripts for risk exposure aggregation, tail-risk metrics extraction (`PERCENTILE_CONT`), and anomaly detection for credit underwriting pipelines.

### 3. Quantitative Risk & Statistical Modeling Engine
* **`quantitative_risk_analytics.py`**: Hypothesis testing, nonparametric distribution bounds (Cantelli/Chebyshev), Expected Shortfall (ES), and historical/parametric Value at Risk (VaR) modeling engine.
* **`snowball_pricing_and_risk.py`**: Monte Carlo simulation engine tracking barrier conditions, knock-in/knock-out probability distribution, and tail losses for structured products.

---

## 💻 Tech Stack
* **Languages & Querying**: Python (Pandas, NumPy, SciPy, Scikit-learn), SQL (PostgreSQL / MySQL)
* **Risk Methodologies**: Monte Carlo Simulation, Value at Risk (VaR), Stress Testing, Credit Scoring Guardrails, Cash-Flow Waterfall Modeling

---
**Contact**: Miao Yang | my2829@columbia.edu | [LinkedIn Profile](https://www.linkedin.com/in/miaoyangdata)
