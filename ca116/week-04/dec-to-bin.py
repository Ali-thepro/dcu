#!/usr/bin/env python3


n = int(input())
output = ""
base = 2

while 0 < n:      # or n != 0 instead of 0 < n
    output = (str(n % base) + output)
    n = n // base

print(output)


# n = int(input())
# b = 0
# i = 0

# while n != 0:
#     r = n % 2
#     n = n // 2
#     b = (r * (10 ** i)) + b
#     i += 1

# print(b)



# decimal = int(input())
# binary = ""

# while decimal != 0:
#     binary = (str(decimal % 2) + binary)
#     decimal = decimal // 2

# print(binary)

