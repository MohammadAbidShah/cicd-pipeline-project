import pandas as pd

def drop_incomplete_rows(df):
    clean_df = df.dropna(subset=['quantity', 'unit_price'])
    return clean_df

def add_revenue_column(df):
    df["revenue"] = df["quantity"] * df["unit_price"]
    return df


def validate(df):
  if len(df) == 0:
    raise ValueError("No rows left after cleaning — something is wrong.")

  if (df["quantity"] <= 0).any():
    raise ValueError("Found a row with zero or negative quantity.")

  if (df["unit_price"] <= 0).any():
    raise ValueError("Found a row with zero or negative price.")