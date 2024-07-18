import pandas as pd
from sklearn.model_selection import train_test_split, learning_curve
from sklearn.pipeline import Pipeline
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer



def split_data(df, target, test_size=0.2):
    X = df.drop(target, axis=1)
    y = df[target]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=0
    )
    return X_train, X_test, y_train, y_test


class Preprocessor:
    """Preprocesses the data of the df before modelisation

    Attributes:
        preprocessor: ...
    """

    def __init__(self, cat_features, num_features) :
        pipe_most_freq_onehot = Pipeline(
            [
                ("imput_most_frequent", SimpleImputer(strategy="most_frequent")),
                (
                    "one_hot",
                    OneHotEncoder(
                        drop="if_binary", sparse=False, handle_unknown="ignore"
                    ),
                ),
            ]
        )
        pip_mean_scale = Pipeline(
            [
                ("imput_mean", SimpleImputer(strategy="mean")),
                ("standard_scaler", StandardScaler()),
            ]
        )

        feature_encoder = ColumnTransformer(
            transformers=[
                ("imp_most_freq_onehot", pipe_most_freq_onehot, cat_features),
                ("imp_mean_scale", pip_mean_scale, num_features),
            ]
        )
        self.preprocessor = feature_encoder

    def fit_transform(self, X):
        return self.preprocessor.fit_transform(X)

    def fit(self, X):
        return self.preprocessor.fit(X)

    def transform(self, X):
        return self.preprocessor.transform(X)

    def get_features_name(self):
        """Retrive features name after preprocessing (usefull for interpretation)"""
        feat_names = []
        for transf in self.preprocessor.transformers_:
            if transf[0] != "remainder":
                names_out = transf[1][-1].get_feature_names_out()
                names_in = transf[2]
                for i, name in enumerate(names_in):
                    names_out_tmp = [
                        c.replace("x%d" % i, "%s" % name) for c in names_out
                    ]
                    names_out = names_out_tmp
                feat_names.extend(names_out)
        return feat_names
