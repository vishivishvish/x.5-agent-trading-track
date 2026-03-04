######################################################################
# Import Packages
######################################################################

import pandas as pd
from config.settings import INITIAL_CAPITAL, BUY_FRACTION, COMMISSION_RATE

######################################################################
# Backtester Engine
######################################################################

class Backtester:

    def __init__(self, strategy):
        self.strategy = strategy

    def run(self, df):

        df = self.strategy.generate_signals(df)

        cash = INITIAL_CAPITAL
        shares = 0

        portfolio_values = []

        for i in range(len(df) - 1):

            today = df.iloc[i]
            tomorrow = df.iloc[i + 1]

            signal = today['signal']
            next_open = tomorrow['Open']

            # BUY
            if signal == 1 and cash > 10:

                capital = cash * BUY_FRACTION
                commission = capital * COMMISSION_RATE
                shares += capital / next_open
                cash -= (capital + commission)

            # SELL
            elif signal == -1 and shares > 0:

                sale_value = shares * next_open
                commission = sale_value * COMMISSION_RATE
                cash += (sale_value - commission)
                shares = 0

            portfolio_value = cash + shares * today['Close']
            portfolio_values.append(portfolio_value)

        # Final day valuation
        final_value = cash + shares * df.iloc[-1]['Close']
        portfolio_values.append(final_value)

        df['portfolio_value'] = portfolio_values

        return df