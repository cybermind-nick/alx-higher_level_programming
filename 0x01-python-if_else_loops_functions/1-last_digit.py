#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = 0
if number < 0:
    temp_num = -1 * number
    num = temp_num % 10
    num *= -1
else:
    num = number % 10

if num < 6 and num != 0:
    print(f"Last digit of {number} is {num} and is less than 6 and not 0")
elif num > 5:
    print(f"Last digit of {number} is {num} and is greater than 5")
else:
    print(f"Last digit of {number} is {num} and is 0")
