#!/usr/bin/env python3

i = 0
smallest = 10000000000

while i < 10:
  n = int(input())
  if n > 0:
    if n < smallest:
      smallest = n
  i += 1
print(smallest)




#!/usr/bin/env python3

# i = 0
# n = 10
# smallpositive = 0

# while i < n:
#   x = int(input())
#   if i == 0 and x > 0:
#     smallpositive = x
#   elif x > 0 and x < smallpositive:
#     smallpositive = x
#   i = i + 1

# print(smallpositive)