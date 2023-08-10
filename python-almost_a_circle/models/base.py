# # models/base.py

# class Base:
#     """
#     This class is the base for all other classes in the project.
#     It manages the 'id' attribute for instances.
#     """

#     __nb_objects = 0

#     def __init__(self, id=None):
#         """
#         Initialize a new instance of the Base class.

#         Args:
#             id (int, optional): If provided, the 'id' attribute of the instance will be set to this value.
#                                If not provided, a unique 'id' will be assigned based on the number of objects created.

#         Returns:
#             None
#         """
#         if id is not None:
#             self.id = id
#         else:
#             Base.__nb_objects += 1
#             self.id = Base.__nb_objects



# models/base.py

class Base:
    """
    This class is the base for all other classes in the project.
    It manages the 'id' attribute for instances.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new instance of the Base class.

        Args:
            id (int, optional): If provided, the 'id' attribute of the instance will be set to this value.
                               If not provided, a unique 'id' will be assigned based on the number of objects created.

        Returns:
            None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
