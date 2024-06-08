#!/usr/bin/env python3

"""
Implement insertion sort.

Implementation taken from:
    MT. Goodrich, R. Tamassia, MH. Goldwasser,
    Data Structures and Algorithms in Python.
    John Wiley and Sons, 1st ed., pp. 150, 2013.
    ISBN: 978-1-118-29027-9
"""


def insertion_sort(sequence):
    """Sort list of comparable elements into nondecreasing order.

    Implementation taken from:
    MT. Goodrich, R. Tamassia, MH. Goldwasser,
    Data Structures and Algorithms in Python.
    John Wiley and Sons, 1st ed., pp. 215, 2013.
    ISBN: 978-1-118-29027-9
    """

    for idx, _ in enumerate(sequence):
        current_element = sequence[idx]
        correct_idx = idx
        while correct_idx > 0 and sequence[correct_idx - 1] > current_element:
            sequence[correct_idx] = sequence[correct_idx - 1]
            correct_idx -= 1
        sequence[correct_idx] = current_element
    return sequence


if __name__ == "__main__":
    test = [-70, 5, -70, 22, 3, 16, 5, 4]
    print(insertion_sort(test))
