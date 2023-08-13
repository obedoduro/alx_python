#!/usr/bin/python3
from models.base import Base

"""This module defines the rectangle class."""
class Rectangle(Base):
    """
    This class represents a rectangle.

    Attributes:
       __width (int): The width of the rectangle
       __height (int): The height of the rectangle
       __x (int): the x-coordinate of the rectangles position
       __y (int): the y-coordinate of the rectangles position
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): The width of the rectangle
            height (int): The heigth of the rectangle
            x (int):  The x-coordinate of the rectangle's position
            y (int): The y-coordinate of the rectangle's position
            id(int): The unique identifier of the rectangle 
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    
    @property
    def width(self):
        """Getter method for __width."""
        return self.__width
    
    @width.setter
    def width(self,value):
        """Setter method for __width"""
        if value <=0:
            raise ValueError("Width must be greater than zero")
        self.__width = value
    
    @property
    def height(self):
        """Getter method for __height."""
        return self.__height
    
    @height.setter
    def height(self,value):
        """Setter method for __height."""
        if value <= 0:
            raise ValueError("Height must be greater than zero")
        self.__height = value

    @property
    def x(self):
        """Getter method for __x"""
        return self.__x
    
    @x.setter
    def x(self,value):
        """Setter method for __x"""
        if value < 0:
            raise ValueError("x must be non-negative")
        self.__x = value
    
    @property
    def y(self):
        """Getter method for __y"""
        return self.__y

    @y.setter
    def y(self,value):
        """Setter method for __y"""
        if value < 0:
            raise ValueError("y must be non-negative")
        self.__y = value
    
rectangle = Rectangle(10, 20, 5, 7, 1)
rectangle.width 
rectangle.height  
rectangle.x  
rectangle.y  
rectangle.id  
