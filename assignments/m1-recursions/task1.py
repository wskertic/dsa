#!/usr/bin/env python3

"""
Task 1 description

Write a recursive function that calculates the factorial of a given
 positive integer n. The factorial of n is the product of all positive
   integers from 1 to n.

For example,
the factorial of 5 is 5 * 4 * 3 * 2 * 1 = 120.

Your function should take one argument, n, and return the factorial of n.
"""


def factorial(n):
    """Recursive implementation of factorial function.

    Implementation taken from:
    MT. Goodrich, R. Tamassia, MH. Goldwasser,
    Data Structures and Algorithms in Python.
    John Wiley and Sons, 1st ed., pp. 150, 2013.
    ISBN: 978-1-118-29027-9
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def test():
    """Execute test cases for task."""
    test_cases = {1: 1, 2: 2, 3: 6, 5: 120, 10: 3628800, 15: 1307674368000}

    print(f"\n{__file__[-8:-3]}\n-----------------------------\n")

    [
        print(f"Factorial {k}:\t{factorial(k)}\n {
            len(str(k))*" "}should be:\t{v}\n")
        for k, v in test_cases.items()
    ]


if __name__ == "__main__":
    test()
