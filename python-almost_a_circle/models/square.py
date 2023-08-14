#!/usr/bin/python3
"""This module defines the rectangle class."""

from models.rectangle import Rectangle
"""
A class returning the square of the rectangle
"""
class Square(Rectangle):
    """
    This class represents a rectangle.

    Attributes:
       __width (int): The width of the rectangle
       __height (int): The height of the rectangle
       __x (int): the x-coordinate of the rectangles position
       __y (int): the y-coordinate of the rectangles position
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): The width of the rectangle
            height (int): The heigth of the rectangle
            x (int):  The x-coordinate of the rectangle's position
            y (int): The y-coordinate of the rectangle's position
            id(int): The unique identifier of the rectangle 
        """

        super().__init__(size, size, x, y, id)


    

    @property
    def size(self):
        """getter for width"""
        return self.width

    @size.setter
    def size(self, value):
        """set value of width to height"""

        if value >=0:            
            self.width = self.height=  value
        else:
            raise ValueError("width must be greater than 0")

    def __str__(self):
        """
        returning area of Square
        """
        return  f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
    