#!/usr/bin/env python3

i = 0
m = 0

while i < 10:
    n = int(input())
    m += n * (10 ** i)
    i += 1

i = 0
while i < 10:
    print(m % 10 ** (10 - i) // 10 ** (10 - 1 - i))
    i += 1


'''
i = 0
quantifier = 1000000000
full_num = 0
while i < 10:
    num = int(input()) * quantifier
    full_num = full_num +num
    quantifier = quantifier // 10
    i = i + 1

i = 0
while i < 10:
    tmp = full_num % 10
    print(tmp)
    full num = full_num // 10
    i = i + 1

'''




'''
n = 10
i = 0
total = 0

while i < n:
   num = int(input())
   total = total * 10 + num
   i = i + 1

i = 0 
while i < n:
   x = total  % 10
   total = total // 10
   print(x)
   i = i + 1

'''