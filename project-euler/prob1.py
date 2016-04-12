#!/usr/bin/env python

"""
Problem 1: Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
import sys
from comtest import TestCase, run_tests

# *****************************************************************************
# FUNCTIONS
# *****************************************************************************

def sum_multi_three_and_five(upper_bound):
    """
    Returns a sum of all multiples of three and 5
    """
    # Remove duplicates by subtracting multiples of 15
    orig_set = multi_of_three_and_five(upper_bound)
    duplicates = [-1 * i for i in multiples_of(15, upper_bound)]
    set = orig_set + duplicates

    return reduce(lambda a, b: a+b, set)

def multi_of_three_and_five(upper_bound):
    """
    Returns a list of multiples of 3 and 5, including duplicates for numbers
    which are multiples of both 3 and 5.
    """
    return multiples_of(3, upper_bound) + multiples_of(5, upper_bound)

def multiples_of(n, upper_bound):
    """
    Return of list of multiples of n upto an upper bound.
    """
    multiples = []
    next = n
    while next < upper_bound:
        multiples.append(next)
        next = next + n
    return multiples

# NOTE(Jeff): Turns out this is a bit faster >=(
def simple(upper_bound):
    sum = 0
    for i in range(upper_bound):
        if i % 3 == 0:
            sum += i
        elif i % 5 == 0:
            sum += i
    return sum

# *****************************************************************************
# SOLUTION
# *****************************************************************************
def solution():
    return sum_multi_three_and_five(1000)

# *****************************************************************************
# MAIN
# *****************************************************************************

if __name__ == "__main__":
    print(solution())
#    testcases = [10, 16, 20, 30, 100, 500, 1000]
#    for t in testcases:
#        print("Optimized = {}, simple = {}".
#              format(sum_multi_three_and_five(t), simple(t)))
#
#     if sys.argv[1] == '1':
#         for i in range(10000):
#             simple(int(sys.argv[2]))
#     else:
#         for i in range(10000):
#             sum_multi_three_and_five(int(sys.argv[2]))



