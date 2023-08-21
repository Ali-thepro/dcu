#!/usr/bin/env python3


s = input()
n = len(s) - 1
total = 0
i = 0

while i < len(s):
    x = int(s[n]) * (2 ** i)
    total += x
    n -= 1
    i += 1

print(total)




# binary = input()
# i = 0
# total = 0
# count = (len(binary) - 1)

# while i < len(binary):
#     if binary[count] == "1":
#         total += (2 ** i)
#     count = count - 1
#     i = i + 1
# print(total)




# s = input()
# i = 0
# total = 0

# while i < len(s):
#     if int(s[i]) == 1:
#         total = total + (2 ** (len(s) - i - 1))
#     i += 1

# print(total)



# bin = input()
# total = 0

# i = 0
# while i < len(bin):
#     total += int(bin[i]) * (2 ** (len(bin) - (i + 1)))
#     i += 1
# print(total)
