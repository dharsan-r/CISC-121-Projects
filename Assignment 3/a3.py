"""
This program contains many different functions that answer each of the
8 questions asked on CISC121 Assignment 3: Recursion

Professor Burton Ma
Author:Dharsan Ravindran
Student ID: 20219218
Date: March 22 ,2021
"""

# The math module is needed by the starter code in Question 7
import math


# Question 1
def zipper(s, t):
    return zipper_helper(s, t, 0, 0)


def zipper_helper(s, t, index_1, index_2):
    if index_1 == len(s):
        return ''
    else:
        return s[index_1] + t[index_2] + zipper_helper(s, t, index_1 + 1, index_2 + 1)


# Question 2
def zipper2(s, t):
    return zipper2_helper(s, t, 0, 0)


def zipper2_helper(s, t, index_1, index_2):
    if index_1 == len(s) and index_2 == len(t):
        return ''
    elif len(s) > len(t) and index_2 == len(t):
        return s[index_1] + zipper2_helper(s, t, index_1 + 1, index_2)
    elif len(t) > len(s) and index_1 == len(s):
        return t[index_2] + zipper2_helper(s, t, index_1, index_2 + 1)
    else:
        return s[index_1] + t[index_2] + zipper2_helper(s, t, index_1 + 1, index_2 + 1)


# Question 3
def is_pow2(n):
    if n == 2 or n == 1:
        return True
    if n > 2:
        return is_pow2(n / 2)
    else:
        return False


# Question 4
def next_pow2(n):
    power = 1
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    elif n > 2:
        return power + next_pow2(n / 2)
    else:
        return power + next_pow2(n // 2)


# Question 5
def max_to_end(t):
    max_to_end_helper(t, 0)


def max_to_end_helper(t, index_1):
    if index_1 == len(t) - 1:
        return
    elif t[index_1] > t[-1]:
        x = t[-1]
        t[-1] = t[index_1]
        t[index_1] = x
    max_to_end_helper(t, index_1 + 1)


# Question 6
def get_enclosed(s):
    if s.startswith('(') and s.endswith(')'):
        return s
    elif len(s) <= 1:
        return ''
    elif not s.endswith(')'):
        return get_enclosed(s[:-1])
    else:
        return get_enclosed(s[1:])


# Question 7
def pretty_print(t):
    for sublist in t:
        for elem in sublist:
            print('{:>4}'.format(elem), end='')
        print()


def to_triangular_grid(t):
    k = len(t)
    if k == 0:
        return [[]]
    n = (-1 + math.sqrt(1 + 8 * k)) / 2
    if not n.is_integer():
        raise ValueError('')
    return to_triangular_grid_impl(t, int(n))


def to_triangular_grid_impl(t, n):
    if n == 1:
        return [t]
    else:
        return [t[0:n]] + to_triangular_grid_impl(t[n:], n - 1)


# Question 8
def triangle_cost(t):
    return triangle_cost_impl(t, 0, 0)


def triangle_cost_impl(t, row, col):
    if row == len(t) - 1 or col == len(t[row]) - 1:
        return t[row][col]

    right = t[row][col] + triangle_cost_impl(t, row, col + 1)
    left = t[row][col] + triangle_cost_impl(t, row + 1, col)

    if left < right:
        return left
    else:
        return right
