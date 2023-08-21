# import sys

# words = sys.stdin.readline()
# words = words.split()
# a = words[0]
# b = words[1]

# lst = []
# for char in a:
#     if char in b:
#         lst.append(char) # p, i, e

# need = lst[-1] # e

# index_a = a.rfind(need) # can also use rindex
# index_b = b.rfind(need) # can also use rindex

# for i in range(len(a)):
#     for j in range(len(b)):
#         if i == index_a:
#             print(b[j], end="")
#         elif j == index_b:
#             print(a[i], end="")
#         else:
#             print(".", end="")
#     print()

# index_need = b.index(need)
# left = "." * index_need 
# right = "." * (len(b) - index_need - 1)
# for char in a:
#     if char != need:
#         print(left + char + right)
#     if char == need:
#         print(b)












#import sys

#first, second = sys.stdin.readline().lower().strip().split()
#letters = [l for l in first if l.isalpha() and l in second]
#firstLast, secondLast = first.rfind(letters[-1]), second.rfind(letters[-1])

#i = 0
#while i < len(first):
#    if i != firstLast:
#        print(("." * secondLast) + first[i] + ("." * (len(second) - 1 - secondLast)))
#    else:
#        print(second)
#    i += 1









# import sys

# for line in sys.stdin:
#     A, B = line.lower().split()
#     seen = []
#     for char in A:
#         if char in B:
#             seen.append(char)
#     a_index = A.rindex(seen[-1])
#     b_index = B.rindex(seen[-1])

# i = 0
# for char in A:
#     leftover = len(B) - b_index - 1
#     if i == a_index:
#         print(B)
#     else:
#         print(("." * b_index) + char + ("." * leftover))
#     i += 1








#!/usr/bin/env python3

# import sys

# for line in sys.stdin:
#     A, B = line.lower().split()
#     for char in A:
#         if char in B:
#             a_index = A.rindex(char)
#             b_index = B.rindex(char)

# for i in range(len(A)):
#     if i == a_index:
#         print(B)
#     else:
#         lines = (list("." * len(B)))
#         lines[b_index] = A[i]
#         print("".join(lines))

# for i in range(len(A)):
#     leftover = len(B) - b_index - 1
#     if i == a_index:
#         print(B)
#     else:
#         print(("." * b_index) + A[i] + ("." * leftover))









#!/usr/bin/env python3

# import sys

# for line in sys.stdin:
#     A, B = line.lower().split()
#     seen = []
#     for char in A:
#         if char in B:
#             seen.append(char)
#     a_index = A.rindex(seen[-1])
#     b_index = B.rindex(seen[-1])


# for i in range(len(A)):
#     if i == a_index:
#         print(B)
#     else:
#         lines = (list("." * len(B)))
#         lines[b_index] = A[i]
#         print("".join(lines))
















#!/usr/bin/env python3

# import sys

# for line in sys.stdin:
#     A, B = line.lower().split()
#     a_index = 0
#     b_index = 0
#     for i in range(len(A)):
#         if A[i] in B:
#             a_index = i
#     for i in range(len(B)):
#         if B[i] == A[a_index]:
#             b_index = i

# length = len(B)
# for i in range(len(A)):
#     if i == a_index:
#         print(B)
#     else:
#         lines = (list("." * length))
#         lines[b_index] = A[i]
#         print("".join(lines))
