#!/usr/bin/env python

"""
Problem 6: Sum square difference

The sum of the squares of the first ten natural numbers is,

   12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,

   (1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.

"""

from comtest import TestCase, run_tests

# *****************************************************************************
# NOTES
# *****************************************************************************
"""
   - how is this a problem?
"""

# *****************************************************************************
# FUNCTIONS
# *****************************************************************************
def sum_of_squares(n):
   tot = 0
   for i in range(1, n+1):
      tot = tot + i * i
   return tot

def square_of_sum(n):
   tot = 0
   for i in range(1, n+1):
      tot = tot + i
   return tot * tot

def sum_of_squares2(n):
   return n*(n+1)*(2*n+1)/6

def square_of_sum2(n):
   return (n*(n+1)/2) * (n*(n+1)/2)

def diff(n):
   return square_of_sum2(n) - sum_of_squares2(n)

# *****************************************************************************
# SOLUTION
# *****************************************************************************
def solution():
   return diff(100)

# *****************************************************************************
# MAIN
# *****************************************************************************
if __name__ == "__main__":
   print(solution())
#    testcases = [
#        TestCase((10,), expected=2640, func=diff),
#    ]
#    run_tests(testcases)
