from sklearn.base import BaseEstimator, TransformerMixin
from .exceptions import ColumnNotFound
import numpy as np
"""
This transformer creates the column "contact" using the "column" argument column
with the default value of "force". The "contact" column is 1 if there is contact
with a surface and 0 if not. The threshold value for determining contact is set
with the "threshold" argument, which is in the same units as the "column"
argument.
"""


class ContactSurface(BaseEstimator, TransformerMixin):

    def __init__(self, column="force", threshold=0.1):
        self.column = column
        self.threshold = threshold

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X_transformed = X.copy()

        # Search for the target column
        if self.column in X.columns:
            # Compute when force is above the contact threshold
            X_transformed["contact"] = np.where(X_transformed[self.column].lt(self.threshold), 0, 1)

            return X_transformed

        else:
            raise ColumnNotFound(f"Column {self.column} not found in "
                                 f"ContactSurface transformer")


def main() -> None:
    pass


if __name__ == "__main__":
    main()
