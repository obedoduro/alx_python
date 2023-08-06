#improve geometry of base geometry
class BaseGeometry:
    def area(self):
        raise Exception('area() is not implemented')

bg = BaseGeometry() 
print(dir(bg))