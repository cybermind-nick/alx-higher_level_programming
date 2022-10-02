#!/bin/usr/python3
"""
    Module Base
    Contains an class Base to serve as a base objects for other classes
"""


class Base:
    """
        class Base
        Args:
            nb_objects (int): instance counter
        Functions:
            __init__(self, id=None)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initials new class instance and increment instance count """
        Base.__nb_objects += 1
        if id is not None:
            self.id = id
        else:
            self.id = __nb_objects
