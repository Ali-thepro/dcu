#!/usr/bin/env python3

a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
s = input()

while s != "end":
    s = int(s)
    a[s] = a[s] + 1
    s = input()

i = 0
while i < len(a):
    print(i, a[i] * "*")
    i += 1




# n = 10
# hist = [0] * n
# line = input()

# while line != "end":
#    hist[int(line)] += 1
#    line = input()

# i = 0
# while i < n:
#    print(i, "*" * hist[i])
#    i = i + 1
