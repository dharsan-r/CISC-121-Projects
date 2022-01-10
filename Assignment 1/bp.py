"""
This program asks the user for their blood pressures and informs them under which
blood pressure category they fall
Author:Dharsan Ravindran
Date: January 2021
Student Id: 20219218
"""

# imports important libraries used in program
import sys

# asks user for their systolic and diastolic blood pressure
systolic = float(sys.argv[1])
diastolic = float(sys.argv[2])

# informs the user that their pressure is normal if the following values are true
if systolic < 120 and diastolic < 80:
    print('normal')
# informs the user that their pressure is prehypertension if one of the following values are true
elif 120 <= systolic < 140 or 80 <= diastolic < 90:
    print('prehypertension')

# informs the user that their pressure is high if one of the following values are true
elif systolic >= 140 or diastolic >= 90:
    print('high blood pressure')
