#!/usr/bin/python3
state = True
for i in range(122, 96, -1):
    if state:
        print("{}".format(chr(i)), end="")
    else:
        print("{}".format(chr(i).upper()), end="")

    state = not state  # toggle
