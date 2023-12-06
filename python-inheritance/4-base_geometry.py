"""
This module should be empty class 
"""


class BaseGeometry():
    """
    Class models  empty class
    """
    def __dir__(cls) -> None:
        """
        access to some inherited attributes
        """
        attributes = super().__dir__()
        n_attributes = []
        for attr in attributes:
            if attr != '__init_subclass__':
                n_attributes.append(attr)
        return n_attributes

    def area(self):
        """Method to raise an exception"""
        raise Exception("area() is not implemented")
