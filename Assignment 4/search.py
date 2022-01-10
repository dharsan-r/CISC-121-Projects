"""
Search related functions for Assignment 4.


Author: Dharsan Ravindran
Student ID: 20219218
Date: April 10, 2021
Instructor: Professor Burton Ma
"""


def sort1000(t):
    aux = [0] * 1000
    for e in t:
        aux[e] += 1
    i=0
    for x in range(1000):
        for y in range(aux[x]):
            t[i] = x
            i+=1


def min_val(t):
    low = 0
    high = len(t) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        if mid == len(t) - 1:
            return t[mid]

        elif mid == 0 and t[mid] > t[mid + 1]:
            return t[mid + 1]

        elif t[mid] < t[mid + 1] and t[mid] < t[mid - 1]:
            return t[mid]

        elif t[mid] < t[mid + 1]:
            high = mid - 1

        # If x is smaller, ignore right half
        elif t[mid] > t[mid + 1]:
            low = mid + 1
