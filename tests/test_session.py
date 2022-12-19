import numpy as np
import pandas

import logits

API_KEY = "not-a-real-api-key"
DATAFRAME = pandas.DataFrame({"col1": [1, 2], "col2": [3, 4]})
NUMPY_ARRAY = np.array([[2, 5], [1, -2]])


def test_sample_df() -> None:
    session = logits.Session(API_KEY)
    session.sample(DATAFRAME)
    pandas.testing.assert_frame_equal(session.data, DATAFRAME)


def test_sample_numpy() -> None:
    session = logits.Session(API_KEY)
    session.sample(NUMPY_ARRAY)
    np.testing.assert_array_equal(session.data, NUMPY_ARRAY)


def test_query() -> None:
    session = logits.Session(API_KEY)
    session.sample(NUMPY_ARRAY)
    assert session.query("not a real instruction") == "TODO"
