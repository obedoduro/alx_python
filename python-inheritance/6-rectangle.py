"""This module improves the class by raising an exception"""


class MetaGeometry(type):
    """class overrides the dir init subclass in the class"""

    def __dir__(cls):
        """Magic method that allows you to override dir"""
        return (attribute for attribute in super().__dir__() if attribute != '__init_subclass__')


class BaseGeometry(metaclass=MetaGeometry):
    """This class defines a base geometry"""

    def area(self):
        """Public instance method that raises an exception"""
        raise Exception("area() is not implemented")

    @staticmethod
    def integer_validator(name, value):
        """public instance method that validates value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """class that inherits BaseGeometry"""

    def __init__(self, width, height):
        """instantiation width and height"""
        self.__width = super().integer_validator('width', width)
        self.__height = super().integer_validator('height', height)
