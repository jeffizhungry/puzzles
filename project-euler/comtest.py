#!/usr/bin/env python

class TestCase(object):
    """
    TestCases helps define, run, and log the output of a single testcase.
    This class aids testers with table driven tests.
    """
    def __init__(self, inputs_tuple, expected, func):
        self.inputs = inputs_tuple
        self.expected = expected
        self.func = func

    def run(self):
        actual = self.func(*self.inputs)
        if actual != self.expected:
            print("[FAIL] {}{} --> (expected {}, got {})".
                    format(self.func.__name__,
                           self.inputs,
                           self.expected,
                           actual))
            return False
        return True

def run_tests(testcases):
    """
    run_tests runs a list of test cases
    """
    all_passed = True
    for t in testcases:
        all_passed = all_passed and t.run()

    if all_passed:
        print("[PASS] Successfully passed all testcases")

