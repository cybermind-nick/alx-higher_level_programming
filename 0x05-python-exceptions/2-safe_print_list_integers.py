#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0) -> int:
    elements_printed = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
            elements_printed += 1
        except ValueError:
            continue
    print()
    return elements_printed
