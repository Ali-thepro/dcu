#!/usr/bin/env python3

m = int(input())
d = int(input())

print(((((m - 1) * 30) + d - 1) % 7) + 1)


# m = int(input()) - 1
# d = int(input()) - 1
# dow = (((m * 30) + d) % 7)
# print(dow + 1)
