#!/usr/bin/python3
def safe_print_list(my_list=[], x=0) -> int:
    elements = 0
    for i in range(x):
        try:
            print(my_list[i], end='')
            elements += 1
        except RangeError:
            print()
            return elements
    print()
    return elements