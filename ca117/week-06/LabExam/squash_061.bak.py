


import sys

output = ''
current_char = ''
count = 0

for char in sys.stdin:
    if char == current_char:
        count += 1
    else:
        if count > 0:
            output += str(count) + current_char
        current_char = char
        count = 1

# Add the count and character for the last character in the string
if count > 0:
    output += str(count) + current_char

print(output)