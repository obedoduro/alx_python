class BaseGeometry:
    def area(self):
        raise Exception ("area() is not implemented")
    
    def integer_validator(self, name, value):

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

bg = BaseGeometry() 
#print(dir(bg))

# print(bg.integer_validator("my_int", 12))

class Rectangle(BaseGeometry):
        
    def __init__(self, width, height):
        self.__width = width
        self.__height =  height 
        self.integer_validator("width", width)
        self.integer_validator("height", height)

rectangle = Rectangle(90, 25)
print(dir(rectangle))  