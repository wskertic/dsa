#!/usr/bin/env python3

"""
Implement merge sort.

Implementations referenced from
    Implementation taken from:
    MT. Goodrich, R. Tamassia, MH. Goldwasser,
    Data Structures and Algorithms in Python.
    John Wiley and Sons, 1st ed., pp. 544 and 547, 2013.
    ISBN: 978-1-118-29027-9
"""

from collections import deque
import math


def merge(sequence1, sequence2, sequence):
    """Merge two sorted queue instances into empty queue (sequence)."""

    while len(sequence1) and len(sequence2):
        if sequence1[0] < sequence2[0]:
            sequence.append(sequence1.popleft())
        else:
            sequence.append(sequence2.popleft())
    if len(sequence1):
        sequence.extend(sequence1)  # move remaining elements
    if len(sequence2):
        sequence.extend(sequence2)  # move remaining elements
    return sequence


def merge_sort(sequence):
    """Sort the elements of queue sequence using the merge-sort algorithm."""

    sequence = deque(sequence)
    n = len(sequence)
    if n < 2:
        return sequence  # list is already sorted
    # divide
    sequence1 = deque()
    sequence2 = deque()
    while len(sequence1) < n // 2:
        sequence1.append(sequence.popleft())
    while len(sequence):
        sequence2.append(sequence.popleft())
    # conquer (with recursion)
    sequence1 = merge_sort(sequence1)  # sort the first half
    sequence2 = merge_sort(sequence2)  # sort the second half
    # merge the results
    sequence = merge(
        sequence1, sequence2, sequence
    )  # merge sorted halves back together
    return sequence


def list_merge(source, result, start, increment):
    """Merge slices of a list into result.

    source[start:start+increment] and source[start+increment:start+2*increment]
    """

    end1 = start + increment  # boundary for run 1
    end2 = min(start + 2 * increment, len(source))  # boundary for run 2
    x, y, z = start, start + increment, start  # index into run 1, run 2, result
    while x < end1 and y < end2:
        if source[x] < source[y]:
            result[z] = source[x]  # copy from run 1 and increment x
            x += 1
        else:
            result[z] = source[y]  # copy from run 2 and increment y
            y += 1
        z += 1  # increment z to reflect new result
    if x < end1:
        result[z:end2] = source[x:end1]  # copy remainder of run 1 to output
    elif y < end2:
        result[z:end2] = source[y:end2]  # copy remainder of run 2 to output


def list_merge_sort(sequence):
    """Sort the elements of python list sequence using the merge-sort algorithm."""

    n = len(sequence)
    logn = math.ceil(math.log(n, 2))
    source, destination = sequence, [None] * n
    for i in (2**k for k in range(logn)):
        for j in range(0, n, 2 * i):
            list_merge(source, destination, j, i)
        source, destination = destination, source
    if sequence is not source:
        sequence[0:n] = source[0:n]
    return sequence


if __name__ == "__main__":
    test = [50, -2, 5, 0, 52, 85, 7]
    print(merge_sort(test))
    print(list_merge_sort(test))
