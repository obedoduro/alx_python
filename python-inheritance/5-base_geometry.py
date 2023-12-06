"""
This module is an empty class 
"""


class BaseGeometry():
    """
    Empty Class models
    """
    def __dir__(cls) -> None:
        """
        Access to some inherited attributes
        """
        attributes = super().__dir__()
        n_attributes = []
        for attr in attributes:
            if attr != '__init_subclass__':
                n_attributes.append(attr)
        return n_attributes

    def area(self):
        """Method to raise an exception with a message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Method that validates value
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
