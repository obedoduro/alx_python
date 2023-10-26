#!/usr/bin/python3
class Square:
    """
    This class represents a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance with the given size.

        Args:
            size (int): The size of the square.

        Returns:
            None
        """
        self.__size = size
    return self.__size

# Example usage
my_square = Square(3)
# print()
# #print(my_square.__dict__)
# my_square_ref = Square
# #print(my_square_ref(3))
# # type(my_square_ref)
def main():
    my_square_ref = my_square
    

main()
__init__