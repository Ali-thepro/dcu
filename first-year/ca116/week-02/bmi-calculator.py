#!/usr/bin/env python3

weight = int(input())
height = int(input())
BMI = weight / (height * height) * 10000

if BMI >= 30:
    print("obese")
elif BMI >= 25:
    print("overweight")
elif BMI >= 18.5:
    print("normal")
elif BMI < 18.5:
    print("underweight")
