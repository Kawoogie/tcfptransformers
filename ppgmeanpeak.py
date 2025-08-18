from sklearn.base import BaseEstimator, TransformerMixin
from scipy import signal
import numpy as np
"""
This transformer computes the mean and peak values of the PPG signal over the
number of data points specified by "interval" on the PPG data series "signal".
"""


class MeanPeakCalculation(BaseEstimator, TransformerMixin):

    def __init__(self, data_set: str, interval=200):
        self.signal = data_set
        self.interval = interval

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X_trans = X.copy()

        if self.signal in X.columns:
            # Determine the names of the new columns
            mean_column_name = self.signal + "_mean"
            peak_colum_name = self.signal + "_peak"

            # Get the number of rows and columns
            rows, columns = X_trans.shape

            # define the filter
            sos_hp = signal.cheby2(2, 50, 0.1, 'hp', fs=200, output='sos')

            # Filter the data
            filtered = signal.sosfilt(sos_hp, X[self.signal])

            for i in range(self.interval, rows):
                X_trans.loc[i, mean_column_name] = np.mean(filtered[i - self.interval:i])
                X_trans.loc[i, peak_colum_name] = np.abs(np.min(filtered[i - self.interval:i])) + np.abs(np.max(filtered[i - self.interval:i]))
        return X_trans


def main() -> None:
    pass


if __name__ == "__main__":
    main()
