"""Module for Geometry Operations."""


class BaseGeometry:
    """
    Base class for geometry-related operations.

    This class is intended to be inherited by other classes representing specific geometric shapes.
    """

    def area(self):
        """
        Calculate the area.

        Raises:
        - NotImplementedError: This method should be implemented by subclasses.
        """
        raise NotImplementedError(
            "Subclasses must implement the 'area' method.")


# Example usage
bg = BaseGeometry()
# Uncommenting the line below would raise a NotImplementedError since 'area' is not implemented in the BaseGeometry class.
# print(bg.area())
