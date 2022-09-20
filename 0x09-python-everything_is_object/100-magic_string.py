#!/usr/bin/python3
def magic_string(s=[]):
    """ using += invokes a reference rather than a copy and updates the real list 's'"""
    s += ["BestSchool"]
    return ", ".join(s)
