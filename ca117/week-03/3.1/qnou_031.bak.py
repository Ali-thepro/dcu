#!/usr/bin/env python3

import sys

print("Words with q but no u:", [c.strip() for c in sys.stdin if 'q' in c.lower().replace('qu', '')])



#!/usr/bin/env python3

# import sys


# result = [word.strip() for word in sys.stdin if word.lower().count("q") > word.lower().count("qu")]
# print("Words with q but no u:", result)




#!/usr/bin/env python3

# import sys

# def isQnou(c):
#     c = c.lower().replace("qu", "")
#     return "q" in c


# output = []
# for line in sys.stdin:
#     line = line.strip()
#     if isQnou(line):
#         output.append(line)


# print(f"Words with q but no u: {output}")