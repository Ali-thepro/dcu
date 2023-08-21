#!/usr/bin/env python3

import sys
field = sys.argv[1]
s = input()
position = 0
start = 0

end = start + 1
while end < len(s) and s[end] != ",":
    end = end + 1

while s[start:end] != field:
    position = position + 1
    start = end + 1

    end = start + 1
    while end < len(s) and s[end] != ",":
        end = end + 1
print(position)




# import sys
# x = int(sys.argv[1])
# s = input()
# a = []
# i = 0


# while i < len(s):
#     if s[i] == ",":
#         a.append(s[:i])
#         s = s[i + 1:]
#         i = 0
#     i = i + 1

# a.append(s)
# print(a[x])

# a.append(s)

# i = 0
# while i < len(a):
#     if a[i] == x:
#         print(i)
#         i = len(a)
#     i = i + 1