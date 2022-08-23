#!/usr/bin/python3
def print_last_digit(number):
    num = 0
    if number < 0:
        temp = -1 * number
        num = temp % 10
        num *= -1
    else:
        num = number % 10

    print("{}".format(num), end="")
