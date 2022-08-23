#!/usr/bin/python3
def remove_char_at(str, n):
    if n == 0:
        print("{}".format(str[1:]))
    else if n == len(str) - 1:
        print("{}".format(str[:n]))
    else:
        print("{}".format(str[:n] + [n+1:]))
