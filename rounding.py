from sklearn.base import BaseEstimator, TransformerMixin

"""
This transformer rounds the values in "column" to the number of
decimal places defined by "precision" using a numerical base "base".
"""


class Rounding(BaseEstimator, TransformerMixin):

    def __init__(self, column: str, precision=3, base=1.0):
        self.column = column
        self.precision = precision
        self.base = base

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X_transformed = X.copy()

        if self.column in X.columns:
            X_transformed[self.column] = X_transformed[self.column].astype(float)
            X_transformed[self.column] = round(self.base * round((X_transformed[self.column])/self.base), self.precision)

        return X_transformed


def main() -> None:
    pass


if __name__ == "__main__":
    main()
