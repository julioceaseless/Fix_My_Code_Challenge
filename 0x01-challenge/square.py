#!/usr/bin/python3
""" lets do some geometry """


class Square:
    """ calculates various properties if a square """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ initialize the square with dimensions"""
        allowed_keys = ['width', 'height']
        if kwargs:
            if "width" in kwargs and "height" in kwargs:
                for key, value in kwargs.items():
                    setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def permiter_of_my_square(self):
        """ calculate the perimeter"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ string representation of the square"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ execute code only when called directly"""
    s = Square(width=12, height=12)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
