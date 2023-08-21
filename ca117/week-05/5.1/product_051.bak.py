#!/usr/bin/env python3

# import sys
# n = sys.stdin.readline().strip()

# while int(n) > 9:
#     product = 1
#     for i in str(n):
#         if i != "0":
#             product *= int(i)
#     n = product
# print(n)




#!/usr/bin/env python3

# import sys

# numstr = sys.stdin.readline().strip()
# def product(numstr):

#     while True:
    

#         digits = [int(c) for c in numstr if int(c) != 0]

#         result = 1
#         for i in digits:
#             result *= i

#         if 1 <= result <= 9:
#             return result
        
#         numstr = str(result)


# print(product(numstr))





#!/usr/bin/env python3

# import sys

# x = sys.stdin.readline()
# integer = int(x)

# while integer > 9:

#     product = 1
#     for digit in str(integer):
#         if digit != "0":
#             product *= int(digit)
#     # continuously changes
#     integer = product
# print(integer)




#!/usr/bin/env python3

# import sys
# num = int(sys.stdin.read().strip())
# s = str(num)

# while len(s) != 1:
# 	total = 1
# 	for n in s:
# 		if int(n) != 0:
# 			total *= int(n)
# 	s = str(total)
# print(s)