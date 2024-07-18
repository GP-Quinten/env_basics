import pandas as pd
import numpy as np
from src import config

def drop_columns(df):
    """Drops useless columns : id_client & branche.

    Args:
        df (dtype): initial pandas dataframe

    Returns:
        dtype: modified dataframe df
    """
    df.drop("id_client", axis=1, inplace=True)
    df.drop("branche", axis=1, inplace=True)  # we drop branche for sake of simplicity
    return df


def clean_churn(df, target):
    """Drops rows where churn value is missing and maps churn column into 0-1 values.

    Args:
        df (dtype): pandas dataframe

    Returns:
        dtype: modified dataframe df
    """
    df.dropna(subset=[target], inplace=True)
    CHURN_mapping = {"oui": 1, "non": 0}
    df[target] = df[target].map(CHURN_mapping)
    return df


def impute_na(df):
    """Replace all empty values is the dataframe by Nan.

    Args:
        df (dtype): pandas dataframe

    Returns:
        dtype: modified dataframe df
    """
    # replace empty values by Nan
    df = df.replace(r"^\s*$", np.nan, regex=True)
    return df


def clean_interet_compte_epargne_total(df):
    """Converts values of "interet_compte_epargne_total" to numerical values.

    Args:
        df (dtype): pandas dataframe

    Returns:
        dtype: modified dataframe df
    """
    df["interet_compte_epargne_total"] = pd.to_numeric(
        df["interet_compte_epargne_total"]
    )
    return df


def clean_compte_epargne(df):
    """Cleans column "compte_epargne" of the df.

    Args:
        df (dtype): pandas dataframe

    Returns:
        dtype: modified dataframe df
    """
    df.loc[
        (df["cartes_bancaires"] == "medium") & (df["compte_epargne"].isnull()),
        "compte_epargne",
    ] = "oui"
    df.loc[
        (df["cartes_bancaires"] == "premium") & (df["compte_epargne"].isnull()),
        "compte_epargne",
    ] = "oui"
    return df


def clean_var_i(df):
    """Cleans variables 0-30 keeping only 6 and adding 6 new columns of difference.

    Args:
        df (dtype): pandas dataframe

    Returns:
        dtype: modified dataframe df
    """
    # remove correlated variables
    for i in range(1, 18):
        df.drop("var_" + str(i), axis=1, inplace=True)
    for i in range(21, 37):
        df.drop("var_" + str(i), axis=1, inplace=True)
    # transform remaining vars into differences
    df["diff_var_0_19"] = df["var_0"] - df["var_19"]
    df["diff_var_0_20"] = df["var_0"] - df["var_20"]
    df["diff_var_20_38"] = df["var_20"] - df["var_38"]
    df["diff_var_0_38"] = df["var_0"] - df["var_38"]
    return df


def data_preparation(df, target):
    """Prepares the dataframe for EDA.

     Args:
        df (dtype): pandas dataframe

    Returns:
        dtype: modified dataframe df
    """
    df = drop_columns(df)

    df = clean_churn(df, target)

    df = impute_na(df)

    df = clean_interet_compte_epargne_total(df)

    df = clean_compte_epargne(df)

    df = clean_var_i(df)

    return df
