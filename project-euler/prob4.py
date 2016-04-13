#!/usr/bin/env python

"""
Problem 4: Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made from the
product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

from comtest import TestCase, run_tests

# *****************************************************************************
# NOTES
# *****************************************************************************
"""
    - the scope of this question is easy enough to brute force
"""

# *****************************************************************************
# FUNCTIONS
# *****************************************************************************
def is_palindrome(n):
    n_str = '{}'.format(n)
    return n_str == n_str[::-1]

def largest_palindrome():
    ans = 0
    for i in range(100, 999):
        for j in range(100, 999):
            possible_ans = i * j
            if ans < possible_ans and is_palindrome(possible_ans):
                ans = possible_ans
    return ans

# *****************************************************************************
# SOLUTION
# *****************************************************************************
def solution():
    return largest_palindrome()

# *****************************************************************************
# MAIN
# *****************************************************************************
if __name__ == "__main__":
    print(solution())
#     testcases = [
#         TestCase((1, ), expected=True, func=is_palindrome),
#         TestCase((12, ), expected=False, func=is_palindrome),
#         TestCase((121, ), expected=True, func=is_palindrome),
#         TestCase((9009, ), expected=True, func=is_palindrome),
#     ]
#     run_tests(testcases)

