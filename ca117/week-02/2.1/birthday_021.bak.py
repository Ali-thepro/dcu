#!/usr/bin/env python3

# import sys
# import calendar
# lines = sys.stdin.readlines()
# poem = ["Monday and Monday's child is fair of face.", "Tuesday and Tuesday's child is full of grace.", "Wednesday and Wednesday's child is full of woe.", "Thursday and Thursday's child has far to go.", "Friday and Friday's child is loving and giving.", "Saturday and Saturday's child works hard for a living.", "Sunday and Sunday's child is fair and wise and good in every way."]
# def weekday(year, month, day):
#     weekday = poem[calendar.weekday(year, month, day)]
#     return weekday

# for line in lines:
#     line = line.rstrip().split()
#     day, month, year = line
#     print(f'You were born on a {weekday(int(year), int(month), int(day))}')






#!/usr/bin/env python3
# import sys
# import calendar

# day_zero = "Monday's child is fair of face."
# day_one = "Tuesday's child is full of grace."
# day_two = "Wednesday's child is full of woe."
# day_three = "Thursday's child has far to go."
# day_four = "Friday's child is loving and giving."
# day_five = "Saturday's child works hard for a living."
# day_six = "Sunday's child is fair and wise and good in every way."
# born = "You were born on a"

# def week_day():
#   if num_day == 0:
#     return f"{born} Monday and {day_zero}"
#   elif num_day == 1:
#     return f"{born} Tuesday and {day_one}"
#   elif num_day == 2:
#     return f"{born} Wednesday and {day_two}"
#   elif num_day == 3:
#     return f"{born} Thursday and {day_three}"
#   elif num_day == 4:
#     return f"{born} Friday and {day_four}"
#   elif num_day == 5:
#     return f"{born} Saturday and {day_five}"
#   else:
#     return f"{born} Sunday and {day_six}"

# for date in sys.stdin:
#   date = date.strip().split()
#   num_day = calendar.weekday(int(date[2]), int(date[1]), int(date[0]))
#   print (week_day())




#!/usr/bin/env python3

# import sys
# import calendar

# day = int(sys.argv[1])
# month= int(sys.argv[2])
# year = int(sys.argv[3])

# Day_of_year = calendar.weekday(year,month,day)
# Day_of_week = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

# Poem = ["Monday's child is fair of face.","Tuesday's child is full of grace.","Wednesday's child is full of woe.","Thursday's child has far to go.","Friday's child is loving and giving.","Saturday's child works hard for a living.","Sunday's child is fair and wise and good in every way."]
# poem_day_of_the_week = Day_of_week[Day_of_year]
# Poem_line = Poem[Day_of_year]
# print("You were born on a",poem_day_of_the_week,"and",Poem_line)