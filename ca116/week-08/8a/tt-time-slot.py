#!/usr/bin/env python3

s = input()
while s != "end":
  tokens = s.split()
  start = int(tokens[1])
  duration = int(tokens[2])
  end = (start + duration - 1) % 24

  start = str(start) + ":00"
  end = str(end) + ":50"

  print(tokens[0], start, end, " ".join(tokens[3:]))
  s = input()



# timetable = input()

# while timetable != "end":
#   timetable = timetable.split()
#   start = int(timetable[1])
#   duration = int(timetable[2])
#   end = str((start + duration - 1) % 24)
#   timetable[1] = str(start) + ":00"
#   timetable[2] = str(end) + ":50"
#   print(" ".join(timetable))
#   timetable = input()




# s = input()
# while s != "end":
#     a = s.split()
#     if a[1][0] == "0":
#         a[1] = a[1][1:]
#     start = a[1] + ":00"
#     end = str(int(a[1]) + int(a[2]) - 1) + ":50"
#     a[1] = start
#     a[2] = end
#     print(" ".join(a))
#     s = input()
