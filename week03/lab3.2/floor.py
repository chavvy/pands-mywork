#lab 3.2
#a program that takes in a float and outputs an int rounded down using the math module

import math

#prompt for a float number input and rounded down integer
float_input = float(input("Enter a float number: "))
floor_output = math.floor(float_input)

#outputting the rounded number
print("{} floored is {}".format(float_input, floor_output))