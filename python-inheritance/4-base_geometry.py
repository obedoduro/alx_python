"""Module for BaseGeometry class."""


class BaseGeometry:
    """
    A base class for geometry-related operations.

    This class should be inherited by other classes representing specific geometric shapes.
    """

    def area(self):
        """
        Calculate the area.

        Raises:
        - NotImplementedError: This method should be implemented by subclasses.
        """
        raise NotImplementedError(
            "The 'area' method is not implemented in the BaseGeometry class.")


# Example usage
if __name__ == "__main__":
    bg = BaseGeometry()

    try:
        print(bg.area())
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
