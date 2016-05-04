#!/usr/bin/env python

"""
Problem 7: 10 001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10 001st prime number?
"""

from comtest import TestCase, run_tests

# *****************************************************************************
# NOTES
# *****************************************************************************
"""
"""

# *****************************************************************************
# FUNCTIONS
# *****************************************************************************

def generate_seq(upper_bound):
    for i in range(2, upper_bound):
        yield i

def filter_sieve(iter_in, prime):
    for n in iter_in:
        if n % prime != 0:
            yield n

def find_prime(n):
    seq = generate_seq(10000000)
    prime = 1
    for i in range(n):
        prime = seq.next()
        out = filter_sieve(seq, prime)
        seq = out
    return prime


# *****************************************************************************
# SOLUTION
# *****************************************************************************
def solution():
    pass

# *****************************************************************************
# MAIN
# *****************************************************************************
if __name__ == "__main__":
    print(find_prime(1000))
#     testcases = [
#         TestCase((1, 1), expected=2, func=add),
#     ]
#     run_tests(testcases)
