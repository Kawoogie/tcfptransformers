from sklearn.base import BaseEstimator, TransformerMixin
from .exceptions import ColumnNotFound
"""
This transformer converts the "force" column in Newtons into a pressure value in
 mmHg into the the column "force". It uses the argument "area" for the 
 computation, which is the area in square mm.
"""

newton_to_mmhg = 7500.62  # N/mm2 to mmHg
contact_area = 142.932  # in mm2


class ComputePressure(BaseEstimator, TransformerMixin):

    def __init__(self, column="force", area=contact_area):
        self.column = column
        self.area = area

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X_transformed = X.copy()

        # Search for the target column
        if self.column in X.columns:
            # Convert the force data to a pressure
            X_transformed['pressure'] = X_transformed[self.column].apply(force_to_pressure)

            return X_transformed
        else:
            raise ColumnNotFound(f"Column {self.column} not found in "
                                 f"ComputePressure transformer.")


def main() -> None:
    pass


# Return the force in mmHg from the Newton input value
def force_to_pressure(force: float, area=contact_area) -> float:
    force_per_area = force/area
    return force_per_area * newton_to_mmhg


if __name__ == "__main__":
    main()
