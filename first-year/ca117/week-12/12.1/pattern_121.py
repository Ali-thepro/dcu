import sys
from re import findall

pattern = sys.stdin.readline().strip()

pattern = r'\b' + pattern.replace('-', r'\w') + r'\b'

text = sys.stdin.read().strip()
matches = findall(pattern, text)

if len(matches) > 0:
    print(", ".join([m for m in matches]))