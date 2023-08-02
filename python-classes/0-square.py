class Square:
    def __init__(self, size):
        self.__size = size

# Example usage
my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)
