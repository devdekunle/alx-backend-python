#!/usr/bin/env python3
add = __import__('0-add').add

print(add(1, 2) == 1 + 2)
print(add.__annotations__)
