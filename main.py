######################################################################
# Import Packages
######################################################################

import pandas as pd
from strategies.mean_reversion import MeanReversionStrategy
from engine.backtester import Backtester
from analytics.performance import compute_performance
from analytics.benchmark import buy_and_hold
from config.settings import INITIAL_CAPITAL

######################################################################
# Main Execution Script
######################################################################

# Load data
df = pd.read_csv("data/raw/tsla.csv")
df['Date'] = pd.to_datetime(df['Date'])

# Initialize strategy & backtester
strategy = MeanReversionStrategy()
bt = Backtester(strategy)

# Run strategy
results = bt.run(df.copy())

# Compute performance
perf = compute_performance(results)

# Compute benchmark
bh = buy_and_hold(df.copy(), INITIAL_CAPITAL)

# Print results
print("\nStrategy Performance:")
print("CAGR (%):", round(perf["CAGR"] * 100, 2))
print("Max Drawdown (%):", round(perf["Max_Drawdown"] * 100, 2))
print("Volatility (%):", round(perf["Volatility"] * 100, 2))
print("Sharpe:", round(perf["Sharpe"], 3))

print("\nBuy & Hold Performance:")
print("CAGR (%):", round(bh["CAGR"] * 100, 2))
print("Max Drawdown (%):", round(bh["Max_Drawdown"] * 100, 2))
print("Volatility (%):", round(bh["Volatility"] * 100, 2))
print("Sharpe:", round(bh["Sharpe"], 3))