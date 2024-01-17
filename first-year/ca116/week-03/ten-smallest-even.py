#!/usr/bin/env python3


n = 10
i = 0
while i < n:
  v = int(input())
  if i == 0 or v < smallest and v % 2 == 0:
    smallest = v
  i = i + 1
print(smallest)


# n = 10
# smallest = int(input())
# i = 0
# while i < n - 1:   #makes n = 9
#   v = int(input())
#   if v < smallest and v % 2 == 0:
#     smallest = v
#   i = i + 1
# print(smallest)