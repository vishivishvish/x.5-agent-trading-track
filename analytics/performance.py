######################################################################
# Import Packages
######################################################################

import numpy as np

######################################################################
# Performance Metrics
######################################################################

def compute_performance(df):

    df['daily_return'] = df['portfolio_value'].pct_change()
    df['daily_return'] = df['daily_return'].fillna(0)

    df['running_peak'] = df['portfolio_value'].cummax()
    df['drawdown'] = (
        (df['portfolio_value'] - df['running_peak'])
        / df['running_peak']
    )

    max_drawdown = df['drawdown'].min()

    total_days = (df['Date'].iloc[-1] - df['Date'].iloc[0]).days
    years = total_days / 365.25

    initial = df['portfolio_value'].iloc[0]
    final = df['portfolio_value'].iloc[-1]

    cagr = (final / initial) ** (1 / years) - 1
    volatility = df['daily_return'].std() * np.sqrt(252)
    sharpe = cagr / volatility if volatility != 0 else 0

    return {
        "CAGR": cagr,
        "Max_Drawdown": max_drawdown,
        "Volatility": volatility,
        "Sharpe": sharpe
    }