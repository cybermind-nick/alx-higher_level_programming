#!/usr/bin/python3
def uniq_add(my_list=[]):
    added = []
    sum = 0
    for i in my_list:
        if i in added:
            continue
        else:
            sum += i
            added.append(i)

    return sum
