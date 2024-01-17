#!/usr/bin/env python3

timetable = input()
timetables = []
while timetable != "end":
    timetables.append(timetable)
    timetable = input()
day = input()
i = 0

while i < len(timetables):
    if timetables[i][0] == day:
        print(timetables[i])
    i = i + 1
