# Library/performance.py
import pandas as pd
import numpy as np
from Library.price import getTickerPrice  # Import from the same package

# Function to calculate trade performance metrics
def calculate_trade_performance(trades: pd.DataFrame) -> pd.Series:
    # Ensure the DataFrame has the correct columns
    required_columns = ['Date', 'Symbol', 'Side', 'Size', 'Price']
    for col in required_columns:
        if col not in trades.columns:
            raise ValueError(f"Missing required column: {col}")

    # Fill missing Size values with 1
    trades['Size'].fillna(1, inplace=True)

    # Calculate current market price for each trade
    trades['Current Price'] = trades.apply(lambda row: getTickerPrice(row['Symbol'], row['Date']), axis=1)
    
    # Calculate P&L for each trade
    trades['P&L'] = np.where(trades['Side'] == 'buy',
                             trades['Size'] * (trades['Current Price'] - trades['Price']),
                             trades['Size'] * (trades['Price'] - trades['Current Price']))

    # Calculate metrics
    total_pnl = trades['P&L'].sum()
    win_rate = (trades['P&L'] > 0).mean() * 100
    avg_pnl = trades['P&L'].mean()
    max_drawdown = (trades['P&L'].cumsum() - trades['P&L'].cumsum().cummax()).min()
    returns = trades['P&L'] / (trades['Size'] * trades['Price'])
    sharpe_ratio = returns.mean() / returns.std() * np.sqrt(252) if returns.std() != 0 else np.nan
    sortino_ratio = returns.mean() / returns[returns < 0].std() * np.sqrt(252) if returns[returns < 0].std() != 0 else np.nan
    cumulative_return = (trades['P&L'].sum() / (trades['Size'] * trades['Price']).sum())
    volatility = returns.std()
    trade_frequency = len(trades)
    exposure_time = (trades['Date'].max() - trades['Date'].min()).days
    
    # Collect metrics in a dictionary
    metrics = {
        'Total P&L': total_pnl,
        'Win Rate': win_rate,
        'Average P&L per Trade': avg_pnl,
        'Max Drawdown': max_drawdown,
        'Sharpe Ratio': sharpe_ratio,
        'Sortino Ratio': sortino_ratio,
        'Cumulative Return': cumulative_return,
        'Volatility': volatility,
        'Trade Frequency': trade_frequency,
        'Exposure Time (days)': exposure_time
    }
    
    return pd.Series(metrics)
