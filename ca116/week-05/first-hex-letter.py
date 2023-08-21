#!/usr/bin/env python3


digits = "0123456789abcdef"
n = int(input())
output = ""
base = 16

while 0 < n:      # or n != 0 instead of 0 < n
    output = digits[n % base] + output
    n = n // base


i = 0
while i < len(output) and not ("a" <= output[i] and output[i] <= "f"):
  i += 1

if i < len(output):
  print(output[i])





#!/usr/bin/env python3

# n = int(input())
# h = ""
# i = 0
# strings = "0123456789abcdef"

# while n != 0:
#     r = strings[n % 16]
#     n = n // 16
#     h = r + h
#     i += 1

# i = 0
# while i < len(h) and not ("a" <= h[i] and h[i] <= "f"):
#   i += 1

# if i < len(h):
#   print(h[i])

