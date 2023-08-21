#!/usr/bin/env python3


s = input()

i = 0
while i < len(s) and not (s[i] >= "0" and s[i] <= "9"):
  i = i + 1

j = i
while j < len(s) and s[j] >= "0" and s[j] <= "9":
  j = j + 1

i = j
while i < len(s) and not (s[i] >= "0" and s[i] <= "9"):
  i = i + 1

j = i
while j < len(s) and s[j] >= "0" and s[j] <= "9":
  j = j + 1

if i < len(s):
  print(s[i:j], i)




# s = input()
# output = ""
# i = 0

# while i < len(s) and (s[i] < "0" or "9" < s[i]):   Finds number
#     i = i + 1

# while i < len(s) and ("0" <= s[i] <= "9"):         Finds end of number
#     i = i + 1

# while i < len(s) and (s[i] < "0" or "9" < s[i]):   Finds Number
#     i = i + 1

# if i < len(s):
#     j = i
#     while j < len(s) and ("0" <= s[j] <= "9"):
#       output += s[j]
#       j += 1
#     print(output, i)





#!/usr/bin/env python3

# s = input()

# i = 0
# while i < len(s) and not (s[i] >= "0" and s[i] <= "9"):
#     i = i + 1

# j = i
# while j < len(s) and (s[j] >= "0" and s[j] <= "9"):
#     j = j + 1

# k = j
# while k < len(s) and not (s[k] >= "0" and s[k] <= "9"):
#     k = k + 1

# i = k
# while i < len(s) and (s[i] >= "0" and s[i] <= "9"):
#     i = i + 1

# if k < len(s):
#     print(s[k:i], k)






#!/usr/bin/env python3

# s = input()

# i = 0
# while i < len(s) and (s[i] <= "0" or "9" <= s[i]):
#     i += 1

# j = i
# if i < len(s):
#     while j < len(s) and ("0" <= s[j] or s[j] >= "9"):
#         j += 1

# m = j
# if j < len(s):
#     while m < len(s) and (s[m] < "0" or "9" < s[m]):
#         m += 1

# k = m
# if m < len(s):
#     while k < len(s) and ("0" <= s[k] or s[k] >= "9"):
#         k += 1

# if m < len(s):
#     print(s[m:k], m)