#!/usr/bin/env python3

import sys
tokens = sys.stdin.read().split()

points = {}
N = 20

i = 0
while i < len(tokens) // 2:
    x = (tokens[i * 2])
    y = (tokens[i * 2 + 1])
    key = x + "/" + y
    points[key] = True
    i = i + 1

print(" " + N * "-")
y = 0
while y < N:
    line = ["|"]
    x = 0
    while x < N:
        key = str(x) + "/" + str(N - y - 1)
        if key in points:
            line.append("*")
        else:
            line.append(" ")
        x = x + 1

    line.append("|")
    print("".join(line))
    y = y + 1
print(" " + N * "-")






#!/usr/bin/env python3

# import sys

# s = sys.stdin.readlines()
# i = 0
# points = {}
# while i < len(s):
#     point = "-".join(s[i].rstrip().split())
#     points[point] = True
#     i = i + 1

# print(" " + "-" * 20)
# y = 0
# while y < 20:
#     x = 0
#     line = "|"
#     while x < 20:
#         if str(x) + "-" + str(20 - y - 1) in points:
#             line = line + "*"
#         else:
#             line = line + " "
#         x = x + 1
#     line = line + "|"
#     print(line)
#     y = y + 1
# print(" " + "-" * 20)

