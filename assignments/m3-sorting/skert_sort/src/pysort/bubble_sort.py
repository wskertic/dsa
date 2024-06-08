#!/usr/bin/env python3

"""
Implement bubble sort.
"""


def bubble_sort(sequence):
    """Sort the list in non-decreasing order.

    Iteratively compare pairs of list elements, swapping elements if unsorted.
    """

    for _ in sequence:
        for idx, val in enumerate(sequence):
            if idx + 1 == len(sequence):  # stop on last element
                break
            if sequence[idx] > sequence[idx + 1]:
                sequence[idx], sequence[idx + 1] = sequence[idx + 1], sequence[idx]
    return sequence


if __name__ == "__main__":
    test = [1, 2, 3, 6, 5, 4]
    print(bubble_sort(test))
