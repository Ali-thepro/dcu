#!/usr/bin/env python3


s = input()
i = 0
while s[i] < "a" or s[i] > "g":
    i = i + 1
print(s[i])



# i = 0
# s = input()
# running = True

# while running:
#     if "a" <= s[i] <= "g":
#         print(s[i])
#         running = False
#     i += 1



# s = input()
# i = 0

# while i < len(s) and "a" > s[i] or s[i] > "g":
#   i = i + 1

# print(s[i])
