#!/usr/bin/python3
"""
class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class def
    """
    def __init__(self, width, height):
        """
        def func
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """
        func def
        """
        return self.__width * self.__height

    def __str__(self):
        """
        def fun
        """
        return '[Rectangle] ' + str(self.__width) + '/' + str(self.__height)
