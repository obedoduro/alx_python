class Square:
    """class to handle square of values 
    pass and return the shit
    Attributes:
    size    The value passed to be squared.
    """
    def __init__(self, size=0):
        """ initialisation of function to handle prerequire values"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = size
        
     

my_square_ref = Square
print(my_square_ref(3))
# type(my_square_ref)
