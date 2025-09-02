from sklearn.base import BaseEstimator, TransformerMixin
from .exceptions import ColumnNotFound
"""
This transformer computes the mean arterial pressure using the systolic and 
diastolic information.
"""


class MAPCalculation(BaseEstimator, TransformerMixin):

    def __init__(self):
        self.sys = "sys"
        self.dia = "dia"

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X_trans = X.copy()

        if (self.sys in X.columns) and (self.dia in X.columns):
            new_column = "map"
            X_trans[new_column] = X_trans[self.dia] + ((1/3) * (X_trans[self.sys] - X_trans[self.dia]))

            return X_trans
        else:
            raise ColumnNotFound(f"Either {self.dia} or {self.sys} not found "
                                 f"using MAPCalculation transformer. Unable to "
                                 f"compute MAP")


def main() -> None:
    pass


if __name__ == "__main__":
    main()
