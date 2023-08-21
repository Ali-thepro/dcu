#!/usr/bin/env python3


digits = "0123456789abcdef"
n = int(input())
output = ""
base = 16

while 0 < n:      # or n != 0 instead of 0 < n
    output = digits[n % base] + output
    n = n // base

print(output)



# n = int(input())
# h = ""
# i = 0
# map = "0123456789abcdef"

# while n != 0:
#     r = map[n % 16]
#     n = n // 16
#     h = r + h
#     i += 1

# print(h)




# dec = int(input())
# hex = ""

# i = 0
# while dec != 0:
#     n = (str(dec % 16))
#     if n == "10":
#         n = "a"
#     elif n == "11":
#         n = "b"
#     elif n == "12":
#         n = "c"
#     elif n == "13":
#         n = "d"
#     elif n == "14":
#         n = "e"
#     elif n == "15":
#         n = "f"
#     hex = n + hex
#     dec //= 16
#     i += 1
# print(hex)
