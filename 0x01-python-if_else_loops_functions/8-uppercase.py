#!/usr/bin/python3
def uppercase(str):
    for i in str:
        out = chr(ord(i) - 32) if ord(i) >= 97 and ord(i) <= 123 else i
        print("{}".format(out), end="")

print()
