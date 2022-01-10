"""
This program
Author:Dharsan Ravindran
Date: January 2021
Student Id: 20219218
"""

import sys
import random

n = int(sys.argv[1])
x= 0
y=0
c=0
for a in range(n):
    x = random.uniform(-1.0,1.0)
    y = random.uniform(-1.0,1.0)
    if (x**2)+(y**2)<=1:
        c+=1
print(str((4*c)/n))