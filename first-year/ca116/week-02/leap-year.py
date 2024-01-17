#!/usr/bin/env python3

n = int(input())
is_leap_year = (n % 400 == 0) or (n % 4 == 0 and n % 100 != 0)
print(is_leap_year)
