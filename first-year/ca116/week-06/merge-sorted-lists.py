#!/usr/bin/env python3

a = []
b = []

s = input()

while s != "end":
    a.append(int(s))
    s = input()

s = input()

while s != "end":
    b.append(int(s))
    s = input()

i = 0
j = 0
while i < len(a) and j < len(b):
    if a[i] < b[j]:
        print(a[i])
        i = i + 1
    else:
        print(b[j])
        j = j + 1


while i < len(a):
        print(a[i])
        i = i + 1

while j < len(b):
    print(b[j])
    j = j + 1


#!/usr/bin/env python3

# a = []
# b = []

# x = input()

# while x != "end":
#     a.append(int(x))
#     x = input()

# x = input()

# while x != "end":
#     b.append(int(x))
#     x = input()

# i = 0
# j = 0
# while i < len(a) and j < len(b):
#     if a[i] < b[j]:
#         print(a[i])
#         i += 1
#     else:
#         print(b[j])
#         j += 1


# if i == len(a):
#     while j < len(b):
#         print(b[j])
#         j += 1
# else:
#     while i < len(a):
#         print(a[i])
#         i += 1




# a = []
# s = input()
# while s != "end":
#     a.append(int(s))
#     s = input()

# s = input()
# while s != "end":
#     a.append(int(s))
#     s = input()

# i = 0
# while i < len(a):
#     p = i
#     j = i + 1
#     while j < len(a):
#         if a[j] < a[p]:
#             p = j
#         j = j + 1
    
#     tmp = a[p]
#     a[p] = a[i]
#     a[i] = tmp
#     i = i + 1

# i = 0
# while i < len(a):
#     print(a[i])
#     i = i + 1