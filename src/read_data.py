import pandas as pd
from transform import drop_incomplete_rows, add_revenue_column, validate

df = pd.read_csv("data/sample_sales.csv")
print("Rows read:", len(df))

clean_df = drop_incomplete_rows(df)
print("Rows after cleaning:", len(clean_df))

final_df = add_revenue_column(clean_df)
validate(final_df)
print("Validation passed")
print(final_df)