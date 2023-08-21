import sys

lines = sys.stdin.readlines()
d = {}
for line in lines:
    line = line.strip().split()
    line = set(line)
    for species in line:
        if species not in d:
            d[species] = 1
        else:
            d[species] += 1
animals = [animal for animal,freq in d.items() if freq == len(lines)]
print(len(animals))
for i in sorted(animals):
    print(i)