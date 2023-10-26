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

# Example usage
my_square = Square(3)
#print(type(my_square))
#print(my_square.__dict__)
