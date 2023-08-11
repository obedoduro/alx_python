#!/usr/bin/python3
"""This module defines the Base class."""

#from models.base import Base

class Base():
    """
    This class represents a rectangle.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
        __x (int): The x-coordinate of the rectangle's position.
        __y (int): The y-coordinate of the rectangle's position.
    """

    def __init__(self, id=None):
        self.id = None
        """
        Initializes a Base instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle's position.
            y (int): The y-coordinate of the rectangle's position.
            id (int): The unique identifier of the rectangle.

        Raises:
            ValueError: If width, height, x, or y is less than 0.
        """
        #super().__init__(id)

# Example usage
rectangle1 = Base()  # Creating an instance without passing an id
rectangle1.id  # This will be automatically assigned (1)

rectangle2 = Base(10)  # Creating an instance with a specific id
rectangle2.id   # This will be 10

rectangle3 = Base()  # Creating another instance without passing an id
rectangle3.id  # This will be automatically assigned (2)

rectangle4 = Base()  # Creating yet another instance without passing an id
rectangle4.id  # This will be automatically assigned (3)