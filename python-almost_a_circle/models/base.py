"""python3 -c 'print(__import__("my_module").__doc__)'"""
"""python3 -c 'print(__import__("my_module").MyClass.__doc__)'"""
class Base:
  
    __nb_objects = 0
    
    """"python3 -c 'print(__import__("my_module").my_function.__doc__)'"""
    """ python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'"""
    def __init__(self, id=None):
       
        if id is not None:
            self.id = id

        # """
        # else  id = None
        # """
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
