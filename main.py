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
for k, v in perf.items():
    print(k, round(v * 100 if "Drawdown" not in k else v * 100, 2))

print("\nBuy & Hold Performance:")
for k, v in bh.items():
    print(k, round(v * 100 if "Drawdown" not in k else v * 100, 2))