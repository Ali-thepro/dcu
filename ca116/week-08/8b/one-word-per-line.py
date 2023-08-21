#!/usr/bin/env python3

import sys

text = sys.stdin.read()
words = text.split()

print("\n".join(words))
