# main.py
import pandas as pd
from Library import calculate_trade_performance
from sample_data import get_sample_data

# Sample DataFrame for testing
trades_df = get_sample_data()

# Calculate metrics
metrics = calculate_trade_performance(trades_df)
print(metrics)
