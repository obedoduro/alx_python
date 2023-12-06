"""Module for checking class relationships."""


def inherits_from(obj, a_class):
    """
    Check if the object is a subclass of the specified class.

    Parameters:
    - obj: The object to check.
    - a_class: The class to compare the object's type with.

    Returns:
    - True if the object is a subclass of the specified class, False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) != a_class

# Parent class


class A:
    """Parent class A."""
    pass

# Inherited directly


class B(A):
    """Inherited class B."""
    pass

# Inherited indirectly


class C(B):
    """Inherited class C, indirectly from A."""
    pass

# Another class


class D:
    """Class D."""
    pass


# Assign objects
obj1 = A()
obj2 = B()
obj3 = C()
obj4 = D()

# Test the function
result1 = inherits_from(obj1, A)  # False, obj1 is not a subclass of A
result2 = inherits_from(obj2, A)  # True, obj2 is a subclass of A
result3 = inherits_from(obj3, A)  # True, obj3 is a subclass of A through B
result4 = inherits_from(obj4, A)  # False, obj4 is not a subclass of A

# Print results
# print(result1)
# print(result2)
# print(result3)
# print(result4)
