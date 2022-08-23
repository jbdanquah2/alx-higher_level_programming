#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = number % 10
s = ""
if n > 5:
    s = "and is greater than 5"
elif n == 0:
    s = "and is 0"
else:
    s = "and is less than 6 and not 0"
print(f"Last digit of {number} is {n} {s}")
