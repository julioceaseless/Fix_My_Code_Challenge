#!/usr/bin/python3
"""
fix the square class
"""


class Square():
    """ class class """

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ initialize class """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def permiter_of_my_square(self):
        return (self.width * 2) + (self.width * 2)

    def __str__(self):
        return "{}/{}".format(self.width, self.width)


if __name__ == "__main__":
    """ run when called directly"""
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
