import sys

pattern = sys.stdin.readline().strip()
lines = sys.stdin.readlines()

indices = []
output = []

for i, char in enumerate(pattern):
    if char == '-':
        indices.append(i)

for line in lines:
    copy = line[:]
    line = list(line.strip())
    for i in indices:
        try:
            line[i] = '-'
        except IndexError:
            pass
    if ''.join(line) == pattern:
        output.append(copy.strip())

if len(output) > 0:
    print(', '.join(output))



# from re import findall

# pattern = r'{:s}'.format(sys.stdin.readline().strip())

# pattern = r'\b' + pattern.replace(r'-', r'\w') + r'\b'

# text = sys.stdin.read()

# matches = findall(pattern, text)

# if matches:
#     print('{:s}'.format(', '.join(matches)))