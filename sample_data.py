# sample_data.py
import pandas as pd

def get_sample_data() -> pd.DataFrame:
    sample_data = {
        'Date': pd.to_datetime(['2024-07-10', '2024-07-12', '2024-07-13']),
        'Symbol': ['AAPL', 'GOOG', 'MSFT'],
        'Side': ['buy', 'sell', 'buy'],
        'Size': [10, 5, 15],
        'Price': [150.0, 2500.0, 200.0]
    }
    return pd.DataFrame(sample_data)
