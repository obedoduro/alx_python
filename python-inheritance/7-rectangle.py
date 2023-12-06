#!/usr/bin/python3
"""
    Base class
"""
BaseGeometry = __import__('5-base_geometry').BaseGeometry


class TypeMetaClass(type):
    """
    A metaclass used to represent the class type inorder to eliminate
    the inherited method init subclass
    """
    def __dir__(cls) -> None:
        """
        Exclude attribute init subclass in dir()
        """
        attributes = super().__dir__()
        return [attribute for attribute in attributes if attribute != '__init_subclass__']


class Rectangle(BaseGeometry, metaclass=TypeMetaClass):
    """
    This is a sub-class of the baseclass
    """

    def __init__(self, width, height):
        """
        Function sets the width and height and ensures
        """
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
