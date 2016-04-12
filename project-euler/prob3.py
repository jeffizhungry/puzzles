#!/usr/bin/env python

"""
Problem 3: Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
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
