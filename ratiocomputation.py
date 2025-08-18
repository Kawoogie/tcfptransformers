from sklearn.base import BaseEstimator, TransformerMixin

"""
This transformer computes the ratio of column_1 to column_2 and saves the result
in a new column titled "column_1_column_2".
"""


class RatioComputation(BaseEstimator, TransformerMixin):

    def __init__(self, column_1: str, column_2: str):
        self.column_1 = column_1
        self.column_2 = column_2

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X_transformed = X.copy()

        if (self.column_1 in X.columns) and (self.column_2 in X.columns):
            new_column = self.column_1 + "_" + self.column_2
            X_transformed[new_column] = X_transformed[self.column_1] / \
                                        X_transformed[self.column_2]

        return X_transformed


def main() -> None:
    pass


if __name__ == "__main__":
    main()
