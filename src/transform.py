import pandas as pd

def drop_incomplete_rows(df):
    clean_df = df.dropna(subset=['quantity', 'unit_price'])
    return clean_df

def add_revenue_column(df):
    df["revenue"] = df["quantity"] * df["unit_price"]
    return df