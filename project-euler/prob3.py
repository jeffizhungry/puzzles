#!/usr/bin/env python

"""
Problem 3: Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600 851 475 143 ?
"""

from comtest import TestCase, run_tests

# *****************************************************************************
# NOTES
# *****************************************************************************
"""
   - attempting to generate all prime number and getting the largest, does not
   work because it is too slow and costs too much memory to generate prime
   numbers upto a number as  as large as 600 billion.

   - attempting to use a generator to save on memory does not work, because
   python eventually hits a recursive depth after adding too many filters
   in the pipeline chain.
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

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def is_prime2(n):
    """
    https://en.wikipedia.org/wiki/Primality_test

    Primality test using trial division with optimizations.
    """
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 ==0 or n % 3 == 0:
        return False

    i = 5

    # only need to check up to sqrt(n)
    while i * i <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i = i + 6

    return True

def largest_prime_factor(n):
    """
    Find the first prime number starting from n and going down to 1.
    """
    i = n
    while i > 1:
        if is_prime2(i):
            if n % i == 0:
                return i
        i -= 1
    return n

def largest_prime_factor2(n):
    """
    Rather than try looking for the biggest prime number from the upper bound.
    Instead attempt to reduce the size of n as much as possible
    """
    i = 2
    while i * i < n:
        if n % i == 0:
            n = n / i
        else:
            i += 1
    return n

# *****************************************************************************
# SOLUTION
# *****************************************************************************
def solution():
    return largest_prime_factor2(600851475143)

# *****************************************************************************
# MAIN
# *****************************************************************************
if __name__ == "__main__":
    print(solution())
#     testcases = [
#         TestCase((1,), expected=1, func=largest_prime_factor2),
#         TestCase((17,), expected=17, func=largest_prime_factor2),
#         TestCase((13195,), expected=29, func=largest_prime_factor2)
#     ]
#     run_tests(testcases)
