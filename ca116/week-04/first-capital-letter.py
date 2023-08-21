#!/usr/bin/env python3

s = input()

i = 0
while s[i] < "A" or s[i] > "Z":
    i = i + 1

print(i)




# s = input()

# i = 0
# while not ("A" <= s[i] and s[i] <= "Z"):
#   i = i + 1

# print(i)
# Loops until capital letter
# Then stops loop and prints i

# i = 0
# s = input()
# running = True

# while running:
#     if "A" <= s[i] <= "Z":
#       print(i)
#       running = False
#     i += 1