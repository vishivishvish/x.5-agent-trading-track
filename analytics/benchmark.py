######################################################################
# Import Packages
######################################################################

import numpy as np

######################################################################
# Buy and Hold Benchmark
######################################################################

def buy_and_hold(df, initial_capital):

    shares = initial_capital / df['Open'].iloc[0]

    df['bh_value'] = shares * df['Close']

    df['bh_daily_return'] = df['bh_value'].pct_change()
    df['bh_daily_return'] = df['bh_daily_return'].fillna(0)

    df['bh_running_peak'] = df['bh_value'].cummax()
    df['bh_drawdown'] = (
        (df['bh_value'] - df['bh_running_peak'])
        / df['bh_running_peak']
    )

    max_dd = df['bh_drawdown'].min()

    total_days = (df['Date'].iloc[-1] - df['Date'].iloc[0]).days
    years = total_days / 365.25

    cagr = (df['bh_value'].iloc[-1] / initial_capital) ** (1 / years) - 1
    volatility = df['bh_daily_return'].std() * np.sqrt(252)
    sharpe = cagr / volatility if volatility != 0 else 0

    return {
        "CAGR": cagr,
        "Max_Drawdown": max_dd,
        "Volatility": volatility,
        "Sharpe": sharpe
    }