import sys
sys.path.append("src")

import pandas as pd
from transform import drop_incomplete_rows

def test_drop_incomplete_rows():
    data = {
        "quantity": [3, None, 5],
        "unit_price": [10.0, 20.0, None]
    }
    df = pd.DataFrame(data)

    result = drop_incomplete_rows(df)

    assert len(result) == 99