#!/usr/bin/python3
"""
    Module 0-lookup

    Contains method lookup that returns list of object's attribute and methods
"""


def lookup(object):
    """ Return the dictionary of an object """
    return dir(object)
