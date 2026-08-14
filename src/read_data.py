import pandas as pd
from transform import add_revenue_column, drop_incomplete_rows

df = pd.read_csv("data/sample_sales.csv")

print("Rows read:", len(df))
print(df)

clean_df = drop_incomplete_rows(df)
print("Rows after cleaning:", len(clean_df))
print(clean_df)

final_df = add_revenue_column(clean_df)
print(final_df)