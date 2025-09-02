"""
Custom exceptions for the package
"""

"""
This exception is used for a call to a column that doesn't exists when 
specifically named by a custom transformer
"""


class ColumnNotFound(Exception):
    def __init__(self, message):
        self.message = message
        # Call the base class constructor with the parameters it needs
        super().__init__(self.message)
