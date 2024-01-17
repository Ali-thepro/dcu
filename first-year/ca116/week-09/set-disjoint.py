#!/usr/bin/env python3

with open("a.txt") as f:
   words1 = f.readlines()
with open("b.txt") as f:
   words2 = f.readlines()

words = words1 + words2
d = {}

i = 0
while i < len(words):
   if words[i] in words1 and words[i] in words2:
      d[words[i].rstrip()] = True
   i = i + 1

if d != {}:
   print("intersecting")
else:
   print("disjoint")









# with open("a.txt") as f:
#    a = f.readlines()
# with open("b.txt") as f:
#    b = f.readlines()

# d = {}

# i = 0
# while i < len(a):
#    if a[i] in b:
#       d[a[i]] = "true"
#    i = i + 1

# if d != {}:
#    print("intersecting")
# if d == {}:
#    print("disjoint")





# #!/usr/bin/env python3

# with open("a.txt") as f:
#     n = f.readlines()
# with open("b.txt") as f_out:
#     m = f_out.readlines()

# files1 = {}
# files2 = {}
# Check = False
# i = 0
# while i < len(n):
#     word = n[i].strip()
#     files1[word] = True
#     i += 1
# i = 0
# while i < len(m):
#     word = m[i].strip()
#     files2[word] = True
#     if word in files2 and word in files1:
#         Check = True
#     i += 1

# if Check is True:
#     print("intersecting")
# else:
#     print("disjoint")




# with open("a.txt") as f:
#     a = f.readlines()
# with open("b.txt") as f:
#     b = f.readlines()

# seen = {}
# i = 0
# while i < len(a):
#     seen[a[i].rstrip()] = True
#     i += 1
# i = 0
# while i < len(b) and b[i].rstrip() not in seen:
#     i += 1
# if i < len(b):
#     intersect = True
# else:
#     intersect = False
# if intersect:
#     print("intersecting")
# else:
#     print("disjoint")
