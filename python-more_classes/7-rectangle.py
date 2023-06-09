#!/usr/bin/python3
"""shebang"""


class Rectangle:
    """ A rectangle with a width and height. """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """inicialization"""

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """return width"""
        return self.__width

    @property
    def height(self):
        """return height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """ Calculet the area"""
        rectanarea = self.__width * self.__height
        return rectanarea

    def perimeter(self):
        """ Calculate Perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        perimeterrectang = (self.__width + self.__height) * 2
        return perimeterrectang

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangulo = ""
        for k in range(self.__height):
            for j in range(self.__width):
                try:
                    rectangulo += str(self.print_symbol)
                except TypeError:
                    rectangulo += type(self.print_symbol)
            if k < (self.__height) - 1:
                rectangulo += "\n"
        return rectangulo

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
