import sys

typed_text = sys.stdin.readline().split()
displayed_text = sys.stdin.readline().split()

sticky_keys = set()
for i in range(len(typed_text)):
    if typed_text[i] == displayed_text[i]:
        continue
    else:
        for letter in displayed_text[i]:
            if displayed_text[i].count(letter) == typed_text[i].count(letter) * 2:
                sticky_keys.add(letter)

print(''.join(sorted(sticky_keys)))
