#!/usr/bin/env python3

"""

"""


from generate_test_inputs import generate_test_input_files
from read_test_inputs import read_test_input_files


def check_for_test_cases():
    """Search test directory for existing test case files."""
    print(read_test_input_files(test_input_sizes=[1]))

def test(test_cases=[3,4,5,6,7], test_answers=[]):
    """Execute test cases for task."""
    check_for_test_cases()


if __name__ == '__main__':
    test() if check_for_test_cases() else generate_test_input_files('nope')