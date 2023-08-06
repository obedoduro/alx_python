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

bg.integer_validator("my_int", 12)