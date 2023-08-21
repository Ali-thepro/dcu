# import sys

# lines = [line.strip() for line in sys.stdin]

# left_side = []
# for index, name in enumerate(lines):
#     if index % 2 == 0:
#         print(name)
#     else:
#         left_side.append(name)


# #for line in left_side[::-1]:
# for name in reversed(left_side):
#     print(name)






# import sys

# lines = [l.strip() for l in sys.stdin.readlines()]
# order = [l for l in lines if len(l) == len(max(lines, key=len))]
# lines = [l for l in lines if len(l) != len(max(lines, key=len))]

# while len(lines) > 0:
#     order.append(lines.pop())
#     order.insert(0, lines.pop())

# for n in order:
#     print(n)





# import sys
# lines = [l.strip() for l in sys.stdin.readlines()]
# left_side = []
# for index, name in enumerate(lines):
#     if index % 2 == 0:
#         print(name)
#     else:
#         left_side.append(name)

# for name in reversed(left_side):
#     print(name)








# import sys

# lines = sys.stdin.readlines()

# evenIndex = [name.strip() for index, name in enumerate(lines) if index % 2 == 0]
# oddIndex = [name.strip() for index, name in enumerate(lines) if index % 2 != 0]

# for name in evenIndex:
#    print(name)
# for name in sorted(oddIndex, key=len, reverse=True):
#    print(name)
