#!/usr/bin/python3
from base import Base

class Rectangle():

    def __init__(self, width, height, x=0, y=0, id=None):
        

        super().base.__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self,value):
        if value <=0:
            raise ValueError("Width must be greater than zero")
        self.__width = value
    
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self,value):
        if value <= 0:
            raise ValueError("Height must be greater than zero")
        self.__height = value

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self,value):
        if value < 0:
            raise ValueError("x must be non-negative")
        self.__x = value
    
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self,value):
        if value < 0:
            raise ValueError("y must be non-negative")
        self.__y = value
    
