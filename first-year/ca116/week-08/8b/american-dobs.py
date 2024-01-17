#!/usr/bin/env python3

with open("irish-dobs.txt") as f:
    lines = f.readlines()

with open("american-dobs.txt", "w") as f:
    i = 0
    while i < len(lines):
        line = lines[i].rstrip().split()
        dates = line[0].split("/")
        tmp = dates[0]
        dates[0] = dates[1]
        dates[1] = tmp
        dates = "/".join(dates)
        name = " ".join(line[1:])
        f.write(dates + " " + name + "\n")
        i = i + 1


#!/usr/bin/env python3

# import sys

# with open("irish-dobs.txt") as f_in:
#     lines = f_in.readlines()
 
# with open("american-dobs.txt", "w") as f_out:
#     i = 0
#     while i < len(lines):
#        tokens = lines[i].split()
#        date = tokens[0].split("/")
#        tokens[0] = "/".join([date[1], date[0], date[2]])  # Replace the date.
#        f_out.write(" ".join(tokens) + "\n")
#        i = i + 1
 