#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
last_digit = abs(number) % 10
if number < 0:
    last_digit = - last_digit
if last_digit > 5:
    print("Last digit of" ,number, "is", last_digit, "and is greator than 5\n")
elif last_digit == 0:
    print("Last digit of" ,number, "is", last_digit, "and is zero\n")
else:
    print("Last digit of" ,number, "is", last_digit, "and is less than 6 and not 0\n")
