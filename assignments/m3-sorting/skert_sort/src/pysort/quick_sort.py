#!/usr/zin/env python3

"""
Implement quick sort.

Implementation from
    Implementation taken from:
    MT. Goodrich, R. Tamassia, MH. Goldwasser,
    Data Structures and Algorithms in Python.
    John Wiley and Sons, 1st ed., pp. 581, 2013.
    ISBN: 978-1-118-29027-9
"""


def inplace_quick_sort(sequence, a=0, z=0):
    """page 581 of the text"""

    if a >= z:
        return
    pivot = sequence[z]
    left = a
    right = z - 1
    while left <= right:
        while left <= right and sequence[left] < pivot:
            left += 1
        while left <= right and pivot < sequence[right]:
            right -= 1
        if left <= right:
            sequence[left], sequence[right] = sequence[right], sequence[left]
            left, right = left + 1, right - 1
    sequence[left], sequence[z] = sequence[z], sequence[left]
    inplace_quick_sort(sequence, a, left - 1)
    inplace_quick_sort(sequence, left + 1, z)
    return sequence


if __name__ == "__main__":
    test = [50, -2, 5, 0, 52, 85, 7]
    print(inplace_quick_sort(test, 0, len(test) - 1))
