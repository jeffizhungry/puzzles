#!/usr/bin/env python

"""
Problem 5: Smallest multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

import math
from comtest import TestCase, run_tests

# *****************************************************************************
# NOTES
# *****************************************************************************
"""

"""

# *****************************************************************************
# FUNCTIONS
# *****************************************************************************
def prime_factors(n):
   factors = []

   i = 2
   while i * i <= n:
      if n % i == 0:
         n = n / i
         factors.append(i)
      else:
         i += 1

   factors.append(int(n))
   return factors

def count(list):
   occurances = {}
   for i in list:
      if i not in occurances:
         occurances[i] = 1
      else:
         occurances[i] += 1

   return occurances

def smallest_multiple(n):
   factors = {}
   for i in range(2,n+1):
      set = count(prime_factors(i))
      for prime in set:
         if prime not in factors or set[prime] > factors[prime]:
            factors[prime] = set[prime]

   ans = 1
   for f in factors:
      ans = ans * math.pow(f, factors[f])

   return int(ans)


# *****************************************************************************
# SOLUTION
# *****************************************************************************
def solution():
   return smallest_multiple(20)

# *****************************************************************************
# MAIN
# *****************************************************************************

if __name__ == "__main__":
   print(solution())
#    testcases = [
#       TestCase((1,), expected=1, func=smallest_multiple),
#       TestCase((2,), expected=2, func=smallest_multiple),
#       TestCase((4,), expected=12, func=smallest_multiple),
#       TestCase((6,), expected=60, func=smallest_multiple),
#       TestCase((10,), expected=2520, func=smallest_multiple),
#    ]
#    run_tests(testcases)
