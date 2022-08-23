#!/usr/bin/python3
state = True
for i in range(123, 96, -1):
    if state:
        print(chr(i), end="")
    else:
        print(chr(i).upper(), end="")

    state = not state  # toggle
