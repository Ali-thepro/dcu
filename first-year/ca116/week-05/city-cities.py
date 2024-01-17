#!/usr/bin/env python3

s = input()

while s != "end":
    i = 0
    while i < len(s) - 5:
        if s[i:i + 4] == "City":
            print(s[:i + 4])
        i += 1
    s = input()




#!/usr/bin/env python3


# b = input()

# while b != "end":
#     i = 0
#     while i < len(b):
#         if b[i:i + 4] == "City" and b[i + 4:i + 5] == ",":
#             print(b[:i + 4])
#         i = i + 1
#     b = input()