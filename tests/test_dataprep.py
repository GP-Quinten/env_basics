from multiprocessing.sharedctypes import Value
import pandas as pd
import numpy as np
import pytest
from src import dataprep
from pandas.api.types import is_numeric_dtype

def test_data_preparation():

    df = pd.DataFrame(
        np.random.randn(20, 39),
        columns=["var_%d" % i for i in range(0, 39)]
    )
    df["interet_compte_epargne_total"] = np.random.randn(20)
    df["interet_compte_epargne_total"].type = "object"
    df["id_client"] = 0
    df["branche"] = "a"
    df["churn"] = 1
    df["compte_epargne"] = 0
    df["cartes_bancaires"] = "premium"

    df = dataprep.data_preparation(df, "churn")
    assert is_numeric_dtype(df["interet_compte_epargne_total"]) == True