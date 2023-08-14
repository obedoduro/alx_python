#!/usr/bin/python3
from models.rectangle import Rectangle
"""
A class returning the square of the rectangle
"""
class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
  

        super().__init__(id)
        super().__init__(x)
        super().__init__(y)
        super().__init__(size)
        super().__init__(size)

        """
        Method returning area of Square
        """

    def __str__(self):
        return "[Square] ({:d}) {:d}/{:d} - {:d} ".format(self.id, self.x, self.y, self.width)

