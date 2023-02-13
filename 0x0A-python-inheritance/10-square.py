#!/usr/bin/python3
"""
module creation
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class
    """
    def __init__(self, size):
        """
        func def
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
