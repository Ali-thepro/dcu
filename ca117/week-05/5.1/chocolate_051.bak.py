#!/usr/bin/env python3

#works for all

import sys

for line in sys.stdin:
    calories = int(line)
    chocolate = 400
    if calories % chocolate == 0:
        print(calories // chocolate)
    elif calories > 0:
        print(calories // chocolate + 1)
    else:
        print("0")




#!/usr/bin/env python3

#works for all


# import sys

# for line in sys.stdin:
#     calories = int(line)
#     if calories == 0:
#         print("0")
#     elif calories < 400:
#         print("1")
#     else:
#         calories = calories + 399
#         print(calories // 400)



#!/usr/bin/env python3

#work for all

# import sys
# import math

# for value in sys.stdin:
#     calories = int(value.strip())
#     bars = math.ceil(calories / 400)
#     print(bars)



# #!/usr/bin/env python3

#Work for all

# import sys


# for line in sys.stdin:
#     chocs = [400]
#     i = 400
#     while i < int(line):
#         i = i + 400
#         chocs.append(i)

#     if int(line) > 0:
#         print(len(chocs))
#     else:
#         print("0")



#!/usr/bin/env python3

#Doesnt work for all


# import sys

# for value in sys.stdin:
#     calories = int(value.strip())
#     bars = round(calories / 400)
#     print(bars)