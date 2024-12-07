import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def clean_data(df):
    # Remove duplicates
    df.drop_duplicates(inplace=True)
    # Handle missing values
    df.fillna(df.mean(), inplace=True)
    return df

def feature_engineering(df):
    # Example: adding a new feature based on existing data
    df['new_feature'] = df['GHI'] / df['Tamb']
    return df
