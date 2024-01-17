#!/usr/bin/env python3

import sys
inputs = sys.stdin.read().strip().split()
t = ''

ends = ['.', '?', '!']

i = 0
while i < len(inputs):
    t += inputs[i]
    if inputs[i][-1] in ends:
        t += '\n'
    else:
        t += ' '
    i += 1

print(t.strip())


#!/usr/bin/env python3

# import sys
# a = sys.stdin.read().split()

# punctuation = {
#     ".": True,
#     "!": True,
#     "?": True,
# }

# i = 0
# j = 0
# while i < len(a):
#     while j < len(a) and a[j][len(a[j]) - 1] not in punctuation:
#         j += 1
#     j += 1
#     print(" ".join(a[i:j]))
#     i = j



#!/usr/bin/env python3

# import sys

# stop_chars = {
#     ".": True,
#     "!": True,
#     "?": True
# }

# text = " ".join(" ".join(sys.stdin.readlines()).split()) + " "

# s = ""
# i = 0
# while i < len(text):
#     s = s + text[i]

#     if text[i] in stop_chars and text[i + 1] == " ":
#         print(s.lstrip())
#         s = ""
#     i = i + 1
