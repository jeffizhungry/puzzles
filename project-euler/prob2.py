#!/usr/bin/env python

"""
Problem 2: Even Fibonacci numbers

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

from comtest import TestCase, run_tests

# *****************************************************************************
# FUNCTIONS
# *****************************************************************************

def sum_even_fib(upper_bound):
    return reduce(lambda a,b: a+b, [i for i in fib(upper_bound) if i % 2 == 0])

def fib(upper_bound):
    set = [1, 2]
    next = set[len(set)-1] + set[len(set)-2]
    while next < upper_bound:
        set.append(next)
        next = set[len(set)-1] + set[len(set)-2]
    return set


# *****************************************************************************
# SOLUTION
# *****************************************************************************
def solution():
    return sum_even_fib(4000000)

# *****************************************************************************
# MAIN
# *****************************************************************************
if __name__ == "__main__":
    print(solution())
#     testcases = [
#         TestCase((10,), expected=10, func=sum_even_fib),
#         TestCase((34,), expected=10, func=sum_even_fib),
#         TestCase((35,), expected=44, func=sum_even_fib),
#     ]
#     run_tests(testcases)
