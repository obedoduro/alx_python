"""Module with a function for checking the instance of an object in a class."""


def is_same_class(obj, a_class):
    """
    Check if the type of the given object is the same as the specified class.

    Parameters:
    - obj: The object to check.
    - a_class: The class to compare the object's type with.

    Returns:
    - True if the object's type is the same as the specified class, False otherwise.
    """
    return type(obj) is a_class

# Classes


class A:
    """Class A."""


class B(A):
    """Class B, which is a subclass of A."""


obj1 = A()
obj2 = B()

result1 = is_same_class(obj1, A)  # True
result2 = is_same_class(obj2, A)  # False
result3 = is_same_class(obj2, B)  # True

# print(result1)
# print(result2)
# print(result3)

a = 1
# print(is_same_class(a, int))  # True
