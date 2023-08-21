#!/usr/bin/env python3

import sys
filename = sys.argv[1]

try:
    # names = []
    highest = 0      # if dont want highest = -1 uncomment names = [] on line 7
    with open(filename) as f:
        for line in f:
            try:
                tokens = line.strip().split()
                studentmark = tokens[0]
                mark = int(tokens[0])
                name = " ".join(tokens[1:])

                if mark > highest:
                    names = []
                    highest = mark
                    names.append(name)

                elif mark == highest:
                    highest = mark
                    names.append(name)

            except ValueError:
                print(f"Invalid mark {studentmark} encountered. Skipping.")

        print(f"Best student(s): {', '.join(names)}")
        print(f"Best mark: {highest}")

except FileNotFoundError:
    print(f"The file {filename} could not be opened.")