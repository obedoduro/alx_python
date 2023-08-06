#parent class
class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

# calculate area
    def area(self):
        return self.__width * self.__height

#details of rectangle
    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"

# Test
rectangle = Rectangle(10, 5)
print(rectangle)
print("Area:", rectangle.area())