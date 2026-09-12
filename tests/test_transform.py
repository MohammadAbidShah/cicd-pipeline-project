import sys
sys.path.append("src")

import pandas as pd
import pytest
from transform import drop_incomplete_rows, validate

def test_drop_incomplete_rows():
    data = {
        "quantity": [3, None, 5],
        "unit_price": [10.0, 20.0, None]
    }
    df = pd.DataFrame(data)

    result = drop_incomplete_rows(df)

    assert len(result) == 1


def test_validate_rejects_negative_quantity():
    bad_data = {
        "quantity": [-2],
        "unit_price": [10.0]
    }
    df = pd.DataFrame(bad_data)

    with pytest.raises(ValueError):
        validate(df)


def test_validate_rejects_zero_price():
    bad_data = {
        "quantity": [3],
        "unit_price": [0.0]
    }
    df = pd.DataFrame(bad_data)

    with pytest.raises(ValueError):
        validate(df)