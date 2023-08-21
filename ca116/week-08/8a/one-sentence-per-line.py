#!/usr/bin/env python3

lines = []

line = input()
while line != "end":
    lines.append(line)
    line = input()

text = " ".join(lines)
sentences = text.split(".")

i = 0
while i < len(sentences):
    sentence = sentences[i]
    words = sentence.split()
    if 0 < len(words):
        print(" ".join(words) + ".")
    i = i + 1
