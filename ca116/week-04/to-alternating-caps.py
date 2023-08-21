#!/usr/bin/env python3

s = input()
t = ""
want_lower_case = True

i = 0
while i < len(s):

   if "A" <= s[i] and s[i] <= "Z" and want_lower_case:
      t = t + chr(ord(s[i]) - ord("A") + ord("a"))

   elif "a" <= s[i] and s[i] <= "z" and not want_lower_case:
      t = t + chr(ord(s[i]) - ord("a") + ord("A"))

   else:
      t = t + s[i]

   if ("A" <= s[i] and s[i] <= "Z") or ("a" <= s[i] and s[i] <= "z"):
      want_lower_case = not want_lower_case

   i = i + 1

print(t)







# s = input()
# t = ""

# want_lower = True

# i = 0
# while i < len(s):
#     is_upper = "A" <= s[i] and s[i] <= "Z"
#     is_lower = "a" <= s[i] and s[i] <= "z"

#     if want_lower and is_upper:
#         t = t + chr(ord("a") + (ord(s[i]) - ord("A")))
#     elif (not want_lower) and is_lower:
#         t = t + chr(ord("A") + (ord(s[i]) - ord("a")))
#     else:
#         t = t + s[i]

#     if is_lower or is_upper:
#         want_lower = not want_lower
#     i = i + 1

# print(t)





# s = input()
# n = 0
# t = ""
# allowCap = False

# i = 0
# while i < len(s):
#     if "A" <= s[i] <= "Z":
#         if not allowCap:
#             t += chr(ord(s[i]) + 32)
#             allowCap = True
#         else:
#             t += s[i]
#             allowCap = False
#     elif "a" <= s[i] <= "z":
#         if allowCap:
#             t += chr(ord(s[i]) - 32)
#             allowCap = False
#         else:
#             t += s[i]
#             allowCap = True
#     else:
#         t += s[i]
#     i += 1

# print(t)





# s = input()
# t = ""
# ShouldBeLower = True

# i = 0
# while i < len(s):
#     if "A" <= s[i] and s[i] <= "Z" and ShouldBeLower:
#         t = t + chr(ord(s[i]) - ord("A") + ord("a"))
#     elif "a" <= s[i] and s[i] <= "z" and not ShouldBeLower:
#         t = t + chr(ord(s[i]) - ord("a") + ord("A"))
#     else:
#         t = t + s[i]
#     if ("A" <= s[i] and s[i] <= "Z") or ("a" <= s[i] and s[i] <= "z"):
#         ShouldBeLower = not ShouldBeLower
#     i = i + 1
# print(t)