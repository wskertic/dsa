#!/usr/bin/env python3

"""
Implement radix sort.

Implentation referenced from https://www.programiz.com/dsa/radix-sort 05-Jun-24.
"""


def counting_sort(sequence, idx):
    """Index elements from sequence by counts to combine."""

    idx = idx if idx else 1
    n = len(sequence)
    counts = [0] * 10
    sorted_sequence = [0] * n

    for i in range(n):
        index = sequence[i] // idx
        counts[index % 10] += 1

    for index in range(1, 10):
        counts[index] += counts[index - 1]

    remaining_index = n - 1
    while remaining_index >= 0:
        index = sequence[remaining_index] // idx
        sorted_sequence[counts[index % 10] - 1] = sequence[remaining_index]
        counts[index % 10] -= 1
        remaining_index -= 1
    return sorted_sequence


def radix_sort(sequence):
    """Apply counting sort iteratively from least significant digit to most."""

    max_element = max(sequence)

    index = 1
    while max_element // index > 0:
        sequence = counting_sort(sequence, idx=index)
        index *= 10
    return sequence


if __name__ == "__main__":
    test = [1, 9, 1, 3, 2, 4, 8, 9, 0, 1421, 1235, 231, 2345, 23, 12, 14, 15]
    print(counting_sort(test, 10))
    print(radix_sort(test))
