#!/usr/bin/python3
"""shebang"""


class BaseGeometry:
    """define a class"""
    pass

    def area(self):

        """area"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
        self.name = name
        self.value = value
