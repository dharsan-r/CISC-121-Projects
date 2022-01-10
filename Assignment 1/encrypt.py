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
message = str(sys.argv[2])

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

if letter > 26:
    letter = letter % 26

cshift_alp = alphabet[letter:len(alphabet)] + alphabet[0:letter]
new_message = ''

for char in message:
    if char in alphabet:
        for n in range(len(alphabet) - 1):
            if char == alphabet[n]:
                new_message += cshift_alp[n]
    else:
        new_message += char

print(new_message)
