#!/usr/bin/env python

"""
Problem 1: Multiples of 3 and 5
#
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
Find the sum of all the multiples of 3 or 5 below 1000.
"""

from comtest import TestCase, run_tests

# *****************************************************************************
# FUNCTIONS
# *****************************************************************************
def add(a, b):
    return a + b

# *****************************************************************************
# SOLUTION
# *****************************************************************************
def solution():
    add(1,1)

# *****************************************************************************
# MAIN
# *****************************************************************************
if __name__ == "__main__":
    testcases = [
        TestCase((1, 1), expected=2, func=add),
        TestCase((2, 2), expected=4, func=add),
        TestCase((3, 3), expected=6, func=add),
    ]
    run_tests(testcases)
