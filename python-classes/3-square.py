#!/usr/bin/python3
"""
Using the @property decorators 
"""
class Square:
    """
    Getting the area size
    """
 
    
    def __init__(self, size=0):
     self.__size = size

    #to retrieve
    @property
    def size(self):
        return self.__size
        
    #size.setter
    @size.setter
    def size(self,value):
        if not isinstance ( value, int):
            raise TypeError("size must be an integer")

        if value<0:
            raise ValueError("size must be >=0")
        self.__size = value
    
    #area of square
    def area(self):
        return self.__size * self.__size




