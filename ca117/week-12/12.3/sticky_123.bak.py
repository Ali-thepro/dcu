import sys

input_str = sys.stdin.readline().strip()
output_str = sys.stdin.readline().strip()

input_str = input_str.replace(' ', '')
output_str = output_str.replace(' ', '')

input_counts = {}
output_counts = {}
for char in input_str:
    input_counts[char] = input_counts.get(char, 0) + 1
for char in output_str:
    output_counts[char] = output_counts.get(char, 0) + 1

sticky_keys = set()
for char, count in output_counts.items():
    if count > input_counts.get(char, 0):
        sticky_keys.add(char)

sticky_keys = ''.join(sorted(sticky_keys))
print(sticky_keys)






# import sys

# input_str = sys.stdin.readline().strip()
# output_str = sys.stdin.readline().strip()

# input_str = input_str.replace(' ', '')
# output_str = output_str.replace(' ', '')

# input_counts = {}
# output_counts = {}
# for char in input_str:
#     if char in input_counts:
#         input_counts[char] += 1
#     else:
#         input_counts[char] = 1
# for char in output_str:
#     if char in output_counts:
#         output_counts[char] += 1
#     else:
#         output_counts[char] = 1

# sticky_keys = set()
# for char, count in output_counts.items():
#     if count > input_counts.get(char, 0):
#         sticky_keys.add(char)

# sticky_keys = ''.join(sorted(sticky_keys))
# print(sticky_keys)





# import sys

# input_str = sys.stdin.readline().strip()
# output_str = sys.stdin.readline().strip()

# input_str = input_str.replace(' ', '')
# output_str = output_str.replace(' ', '')

# input_counts = {}
# output_counts = {}
# for char in input_str:
#     if char in input_counts:
#         input_counts[char] += 1
#     else:
#         input_counts[char] = 1
# for char in output_str:
#     if char in output_counts:
#         output_counts[char] += 1
#     else:
#         output_counts[char] = 1

# sticky_keys = set()
# for char in output_counts:
#     if char in input_counts:
#         if output_counts[char] > input_counts[char]:
#             sticky_keys.add(char)


# sticky_keys = ''.join(sorted(sticky_keys))
# print(sticky_keys)
