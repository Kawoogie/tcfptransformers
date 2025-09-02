from sklearn.base import BaseEstimator, TransformerMixin
from .exceptions import ColumnNotFound
"""
This transformer converts negative values in "column" to zero values. The 
default column is the "force" column.
"""


class RemoveNegatives(BaseEstimator, TransformerMixin):

    def __init__(self, column="force"):
        self.column = column

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X_transformed = X.copy()

        # Search for the target column
        if self.column in X.columns:
            # Convert the force data to a pressure
            X_transformed[self.column] = X_transformed[self.column].clip(lower=0)

            return X_transformed
        else:
            raise ColumnNotFound(f"Column {self.column} not found in "
                                 f"RemoveNegatives transformer")


def main() -> None:
    pass


if __name__ == "__main__":
    main()
