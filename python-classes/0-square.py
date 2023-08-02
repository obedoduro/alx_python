class Square:
    def __init__(self, size):
        self.__size = size

# Example usage
square = Square(3)
print(type(square))
print(square.__dict__)
try:
    print(square.size)
except AttributeError as e:
    print(e)
try:
    print(square.__size)
except AttributeError as e:
    print(e)
