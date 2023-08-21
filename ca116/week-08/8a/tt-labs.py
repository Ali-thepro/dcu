#!/usr/bin/env python3

s = input()
a = []
while s != "end":
    words = s.split()
    if words[2] != "1":
        print(" ".join(words))
    s = input()



# s = input()
# a = []

# while s != "end":
#     s = s.split()
#     a.append(s)
#     s = input()


# i = 0
# while i < len(a):
#     if a[i][2] != "1":
#         print(" ".join(a[i]))
#     i = i + 1
