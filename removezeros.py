from sklearn.base import BaseEstimator, TransformerMixin
from .exceptions import ColumnNotFound
"""
This transformer removes zero points by replacing them with the value of the
point before them. The default removes the zero points on the red, green, and ir
PPG signals
"""


class RemoveZeros(BaseEstimator, TransformerMixin):

    def __init__(self, columns=None):
        if columns is None:
            self.columns = ["green", "red", "ir"]

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X_transformed = X.copy()

        for column in self.columns:
            if column in X.columns:
                X_transformed[column].replace(0, float('nan'), inplace=True)
                X_transformed[column].ffill(inplace=True)

                return X_transformed
            else:
                raise ColumnNotFound(f"In columns: {self.columns}, one of the "
                                     f"columns was not found in the RemoveZeros"
                                     f" transformer")


def main() -> None:
    pass


if __name__ == "__main__":
    main()
