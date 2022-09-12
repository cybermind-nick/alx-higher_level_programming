#!/usr/bin/python3
def safe_print_division(a, b) -> int:
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {}".format(result))
        print("{:d} / {:d} = {}".format(a, b, result))
