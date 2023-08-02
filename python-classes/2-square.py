class Square:
    def __init__(self, size=0):
        if not isinstance(size,int):
           raise TypeError ("size must be an integer")

        if  size < 0:
            raise ValueError ("size must be >=0") 
        self.__size = size

  


    def area(self):
        return self.__size * self.__size 

my_square_1 = Square(3)
print(type(my_square_1))
print(my_square_1.__dict__)