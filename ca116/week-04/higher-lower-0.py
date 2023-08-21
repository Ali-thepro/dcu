#!/usr/bin/env python3

prev = int(input())

while prev != 0:
  curr = int(input())
  if curr == 0:
    curr = curr + 0
  elif curr > prev:
    print("higher")
  elif curr < prev:
    print("lower")
  else:
    print("equal")
  prev = curr



# prev = int(input())
# if prev != 0:
#    curr = int(input())

#    while curr != 0:
#       if curr < prev:
#          print("lower")
#       elif curr == prev:
#          print("equal")
#       else:
#          print("higher")
#       prev = curr
#       curr = int(input())
