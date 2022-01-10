"""
This program prints the value of y for 4  different functions given an x value inputted by user
Author:Dharsan Ravindran
Date: January 2021
Student Id: 20219218
"""

# imports important libraries used in program
import sys
import math

# takes input from user to use in equations
x = float(sys.argv[1])

# formulas for equations 1 and 2
equation_1 = (1 - math.cos(x)) / x ** 2
equation_2 = (2 * math.sin(x / 2) ** 2) / x ** 2

# if else code blocks for the third function, calculated based on x value
if x <= 0:
    equation_3 = 0
elif 0 < x <= 1:
    equation_3 = 3 * (x ** 2) - 2 * (x ** 3)
else:
    equation_3 = 1

# formula for equation 4
equation_4 = (1 / math.sqrt(2 * math.pi)) * math.exp(-((x ** 2) / 2))

# prints the y value for all of the equations
print(equation_1)
print(equation_2)
print(equation_3)
print(equation_4)
