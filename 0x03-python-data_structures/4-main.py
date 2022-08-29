#!/usr/bin/python3
from sys import argv, exit
if len(argv) <= 1:
    exit(0)
my_list = [1,4,5,6,3,2,1]

new_in_list = __import__("4-new_in_list").new_in_list

print("Old list: {}".format(my_list))

new_in_list(my_list, int(argv[1]), int(argv[2]))
print("New list: {}".format(my_list))
