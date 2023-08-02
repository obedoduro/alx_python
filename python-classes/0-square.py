class Square:
    def __init__(self, size):
        self.__size = size

# Example usage
square = Square(3)
print(type(square))

try:
   pass
except AttributeError as e:
    pass
try:
    pass
except AttributeError as e:
    pass
