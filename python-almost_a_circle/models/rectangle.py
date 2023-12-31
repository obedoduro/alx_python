#!/usr/bin/python3
"""This module defines the rectangle class."""
from models.base import Base


class Rectangle(Base):
    """
    This class represents a rectangle.

    Attributes:
       __width (int): The width of the rectangle
       __height (int): The height of the rectangle
       __x (int): the x-coordinate of the rectangles position
       __y (int): the y-coordinate of the rectangles position
    """
    count=0
    countol =0

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
        if not isinstance(value, int):
            raise TypeError ("width must be an integer")

        if value <=0:
            raise ValueError("width must be > 0")
        
        self.__width = value
    
    @property
    def height(self):
        """Getter method for __height."""
        return self.__height
    
    @height.setter
    def height(self,value):
        """Setter method for __height."""
        if not isinstance(value, int):
            raise TypeError ("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")
        
        self.__height = value

    @property
    def x(self):
        """Getter method for __x"""
        return self.__x
    
    @x.setter
    def x(self,value):
        """Setter method for __x"""
        
        if not isinstance(value, int):
            raise TypeError ("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value
    
    @property
    def y(self):
        """Getter method for __y"""
        return self.__y

    @y.setter
    def y(self,value):
        """Setter method for __y"""
        if not isinstance(value, int):
            raise TypeError ("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
       
        self.__y = value

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height
    
    def display(self):
        """Display stdout the Rectangle instance with the character #"""
        if self.__y != 0 :
           print("\n"* ((self.__y)-1))
        else:
            print(end='')

        for _ in range (self.__height):
            print((" "* self.__x), end = '')
            print("#" * self.__width)
            

    def __str__(self):
        """Display # in format of id x y height and width"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)
    
    def update(self, *args, **kwargs):

            
        """
        Assigning arguments to attributes
        
        Args:
            *args: Arguments in the order id, width, height, x and y 
            **kwags: keyword argument represnting attribute key/vlaue pairs.
        """
        if args:

            if len(args) >= 1 :
                self.id = args[0]
            if len(args) >= 2 :
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]

        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    



           
        

# rectangle = Rectangle(10, 12)
# rectangle.width 
# rectangle.height  
# rectangle.x  
# rectangle.y  
# rectangle.id  
# rectangle.area()