######################################################################
# Import packages
######################################################################

import pandas as pd

######################################################################
# Mean Reversion Strategy Class
######################################################################

class MeanReversionStrategy:

    def generate_signals(self, df):
        """
        Generate buy/sell signals using Bollinger Band logic
        """

        df = df.copy()

        # Compute rolling statistics
        df['mu'] = df['Close'].rolling(252).mean().shift(1)
        df['sigma'] = df['Close'].rolling(252).std().shift(1)

        # Create bands
        df['upper_band'] = df['mu'] + 2 * df['sigma']
        df['lower_band'] = df['mu'] - 2 * df['sigma']

        # Initialize signal column
        df['signal'] = 0

        # Buy condition
        df.loc[df['Close'] < df['lower_band'], 'signal'] = 1

        # Sell condition
        df.loc[df['Close'] > df['upper_band'], 'signal'] = -1

        # Remove signals during NaN period
        df.loc[df['mu'].isna(), 'signal'] = 0

        return df