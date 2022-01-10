"""
This program
Author:Dharsan Ravindran
Date: January 2021
Student Id: 20219218
"""

# imports important libraries used in program
import sys

# asks user for the
letter = int(sys.argv[1])

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

if letter>26:
    letter = letter%26


cshift_alp  = alphabet[letter:len(alphabet)] + alphabet[0:letter]

print(cshift_alp)