"""Module for checking class relationships."""


def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of the specified class or a subclass of it.

    Parameters:
    - obj: The object to check.
    - a_class: The class to compare the object's type with.

    Returns:
    - True if the object is an instance of the specified class or a subclass of it, False otherwise.
    """
    return isinstance(obj, a_class) or issubclass(type(obj), a_class)

# Parent class


class A:
    """Parent class A."""
    pass

# Inherited class


class B(A):
    """Inherited class B."""
    pass

# Another class


class C:
    """Class C."""
    pass


# Objects assigned
obj1 = A()
obj2 = B()
obj3 = C()

# Test the function
result1 = is_kind_of_class(obj1, A)  # True, obj1 is an instance of A
result2 = is_kind_of_class(obj2, A)  # True, obj2 is a subclass of A
result3 = is_kind_of_class(obj2, B)  # True, obj2 is an instance of B
result4 = is_kind_of_class(obj3, C)  # True, obj3 is an instance of C
# False, obj3 is not an instance or subclass of A
result5 = is_kind_of_class(obj3, A)

# Test with a non-class object
a = 1
result6 = is_kind_of_class(a, int)  # True, 'a' is an instance of int

# Print results
# print(result1)
# print(result2)
# print(result3)
# print(result4)
# print(result5)
# print(result6)
