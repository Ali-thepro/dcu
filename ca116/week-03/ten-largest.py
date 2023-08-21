#!/usr/bin/env python3

largest = 0
i = 0

while i < 10:
   n = int(input())
   if n > largest:
      largest = n
   i += 1
print(largest)


# i = 0
# largest = 0

# while i < 10:
#    x = int(input())
#    if i == 0 or largest < x:
#       largest = x
#    i = i + 1

# print(largest)