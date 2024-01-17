#!/usr/bin/env python3


n = int(input())
half = n // 2

i = 0
while i < n:
    j = half -i
    if j < 0:
        j = -j
    if j == 0:
        print(half * " " + "*")
    else:
        print((half - j) * " " + "*" + (2 * j - 1) * " " + "*")
    i = i + 1




# n = int(input())
# i = 0
# space = " "

# while i < n:
#     if i == n // 2:
#         print(space * (n // 2) + "*")
#     elif i < n // 2:
#         mid_space = space * ((n - 2 - i) - len((space * i)))
#         print((space * i) + "*" + mid_space + "*")
#     elif i > n // 2:
#         m = 2 * (n // 2 - i) * - 1 - 1
#         print((space * (n - i - 1) + "*" + space * m + "*"))
#     i = i + 1
