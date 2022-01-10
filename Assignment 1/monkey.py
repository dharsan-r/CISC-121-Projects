"""
This program
Author:Dharsan Ravindran
Date: January 2021
Student Id: 20219218
"""

import sys
import random

word = sys.argv[1]
times = int(sys.argv[2])
word_test = ""
repeat = 0
for x in range(times):
    for y in range(len(word)):
        test_letter = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        word_test+=test_letter
    if word_test == word:
        repeat+=1
    word_test=""

print("The string " + word + " was typed " + str(repeat) + " times.")