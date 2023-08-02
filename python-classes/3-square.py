class Square:
    def __init__(self, size=0):
     self.__size = size

    #to retrieve
    def size(self):
        return self.__size
        
    #size.setter
    def size(self,value):
        if not isinstance ( value, int):
            raise TypeError("size must be an integer")

        if value<0:
            raise ValueError("size must be >=0")
        self.__size = value
    
    #area of square
    def area(self):
        return self.__size * self.__size


my_square_1 = Square(0)
print(my_square_1.size)
print(my_square_1.area())