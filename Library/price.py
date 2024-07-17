# Library/price.py
import random
import pandas as pd

# Helper function to get the price of a security on a given date
def getTickerPrice(ticker: str, date: pd.Timestamp) -> float:
    return random.uniform(1, 100)  # Example implementation
