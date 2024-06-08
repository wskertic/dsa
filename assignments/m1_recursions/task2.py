#!/usr/bin/env python3

"""
Task 2 description

Write a recursive function that calculates the nth Fibonacci number,
where n is a positive integer. The Fibonacci sequence is a series of
numbers in which each number is the sum of the two preceding ones,
usually starting with 0 and 1.

For example,
the first 10 numbers in the Fibonacci sequence are: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.

Your function should take one argument, n, and return the nth Fibonacci number.
"""


def good_fibonacci(n):
    """Return pair of Fibonacci numbers, F(n) and F(n-1).

    Implementation taken from:
    MT. Goodrich, R. Tamassia, MH. Goldwasser,
    Data Structures and Algorithms in Python.
    John Wiley and Sons, 1st ed., pp. 167, 2013.
    ISBN: 978-1-118-29027-9
    """
    if n <= 1:
        return (n, 0)
    else:
        (a, b) = good_fibonacci(n - 1)
        return (a + b, a)


def fib_n(n):
    """Wrapper function that returns only the nth Fibonacci number.

    This function relies on a call to the good_fibonacci(n) recursive
    implementation from 'Data Structures & Algorithms in Pyton' published
    by John Wiley and Sons, 1st ed., pp. 167, 2013.
    """
    return good_fibonacci(n)[0]


def test():
    """Execute test cases for task."""

    test_cases = {
        0: 0,
        1: 1,
        3: 2,
        8: 21,
        14: 377,
        28: 317811,
        117: 1264937032042997393488322,
    }

    print(f"\n{__file__[-8:-3]}\n-----------------------------\n")

    [
        print(f"Fibonacci number {k}:\t{fib_n(k)}\n\t{
            len(str(k))*" "}should be:\t{v}\n")
        for k, v in test_cases.items()
    ]


if __name__ == "__main__":
    test()
