from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
"""
This transformer computes the derivatives of the PPG signals listed in "columns"
with green, red, and ir the default. Set the "second_comp" argument to "False"
to not compute the second derivative. 
"""


class RemoveZeros(BaseEstimator, TransformerMixin):

    def __init__(self, columns=None, second_comp=True):
        if columns is None:
            self.columns = ["green", "red", "ir"]
        self.second_comp = second_comp

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X_trans = X.copy()
        rate = 1/200

        for column in self.columns:
            if column in X.columns:

                first = column + "_1"
                second = column + "_2"

                X_trans[first] = np.gradient(X_trans[column], rate, edge_order=1)
                X_trans[second] = np.gradient(X_trans[first], rate, edge_order=1)

        return X_trans


def main() -> None:
    pass


if __name__ == "__main__":
    main()
