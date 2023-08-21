#!/usr/bin/env python3

import sys
x = int(sys.argv[1])
s = input()
a = []
i = 0


while i < len(s):
    if s[i] == ",":
        a.append(s[:i])
        s = s[i + 1:]
        i = 0
    i = i + 1

a.append(s)
print(a[x])





# import sys
# pos = int(sys.argv[1])

# s = input()
# a = []
# running = True

# while running:
#     i = 0
#     tmp_a = []
#     while i < len(s):
#         tmp_str = ""
#         while i < len(s) and s[i] != ",":
#             tmp_str = tmp_str + s[i]
#             i = i + 1
#         tmp_a.append(tmp_str)
#         i = i + 1
#     a.append(tmp_a)
#     s = input()
#     if len(s) > 0:
#         running = True
# print(a[0][pos])