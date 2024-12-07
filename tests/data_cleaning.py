import pandas as pd

def remove_duplicates(df):
    return df.drop_duplicates()

def handle_missing_values(df):
    return df.fillna(df.mean())  # Filling NaN values with column mean
