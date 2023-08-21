#!/usr/bin/env python3

x = int(input())
y = int(input())
z = x % (10 ** (y + 1))
print(z // (10 ** y))
#print(x // (10 ** y) % 10)
#this above print statement works only with line 3 and 4 line 5 is not included