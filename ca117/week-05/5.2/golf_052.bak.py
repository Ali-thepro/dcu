#!/usr/bin/env python3

import sys
disqualified = []
scoress = []
namess = []
nameScore = sys.stdin.readlines()
for name in nameScore:
    name = name.strip()
    scores = name[-5:].split()
    i = 0
    for score in scores:
        if score.strip().isnumeric():
            i += int(score)
        else:
            disqualified.append(name[:-5].strip())
            break
    scoress.append(i)
    namess.append(name[:-6])
    z = zip(namess,scoress)
    d = {n:s for n,s in z}
for disqualify in disqualified:
    d.pop(disqualify)

def tagger(item):
   return item[1]

for k, v in sorted(d.items(), key=tagger):
   print(f'{k}: {v}')
if len(disqualified) > 0:
    print(f'Disqualified: {", ".join(disqualified)}')





#!/usr/bin/env python3

# import sys


# tuples = []
# disqualified = []
# lines = sys.stdin.readlines()
# for line in lines:
#     nums = [int(n) for n in line if n.isnumeric()]

#     line = line.strip().split()
#     if len(nums) != 3:
#         disqualified.append(" ".join(line[:-3]))
#     else:
#         name = " ".join(line[:-3])
#         both = (sum(nums), name)
#         tuples.append(both)
# tuples.sort()
# for result in tuples:
# 	print(f'{result[1]}: {result[0]}')
# # s = ""
# # for i in range(len(disqualified)):
# #     s += " " + disqualified[i] + ",  "
# #     s = s.strip()
# #     if i + 1 == len(disqualified):
# #         print(f'Disqualified: {s[:-1]}')

# if disqualified:
#     print(f'Disqualified: {", ".join(disqualified):s}')

    