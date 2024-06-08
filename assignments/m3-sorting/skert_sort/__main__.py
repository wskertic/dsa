#!/usr/bin/env python3

"""
Performance Testing: After implementing the sorting algorithms, assess their performance
using random data sets of 1,000, 10,000, 100,000, 1,000,000, and 10,000,000 integers
(ranging from 0 to 2,147,483,647). Ensure that the input data are unsorted and that all
algorithms use the identical input file for each input size. Note: If any algorithm takes
more than 20 minutes to sort data, terminate the program and denote this in your report as
"> 20 m".
"""

from pathlib import Path

from src.pysort import bubble_sort, insertion_sort, merge_sort, quick_sort, radix_sort
from tests.read_test_inputs import read_test_input_files
from tests.test_timer import test_timer


def run_timers(function, input_keys, input_sets) -> dict:
    return {
        size: test_timer(function, input) for size, input in zip(input_keys, input_sets)
    }


def bubble(test_sizes: list, runs: int = 1) -> dict:
    """Run test_timer against bubble_sort n times, given n = len(test_sizes) == len(input_sets)"""
    input_sets = read_test_input_files(path=Path(__file__).parent, test_input_sizes=test_sizes)
    return {
        f"run{run}": run_timers(bubble_sort.bubble_sort, test_sizes, input_sets)
        for run in range(1, runs + 1)
    }


def insert(test_sizes: list, runs: int = 1) -> dict:
    """Run test_timer against insertion_sort n times, given n = len(test_sizes) == len(input_sets)"""
    input_sets = read_test_input_files(path=Path(__file__).parent, test_input_sizes=test_sizes)
    return {
        f"run{run}": run_timers(insertion_sort.insertion_sort, test_sizes, input_sets)
        for run in range(1, runs + 1)
    }


def merge(test_sizes: list, runs: int = 1) -> dict:
    """Run test_timer against merge_sort n times, given n = len(test_sizes) == len(input_sets)"""
    input_sets = read_test_input_files(path=Path(__file__).parent, test_input_sizes=test_sizes)
    return {
        f"run{run}": run_timers(merge_sort.merge_sort, test_sizes, input_sets)
        for run in range(1, runs + 1)
    }


def quick(test_sizes: list, runs: int = 1) -> dict:
    """Run test_timer against quick_sort n times, given n = len(test_sizes) == len(input_sets)"""
    input_sets = read_test_input_files(path=Path(__file__).parent, test_input_sizes=test_sizes)
    return {
        f"run{run}": run_timers(quick_sort.inplace_quick_sort, test_sizes, input_sets)
        for run in range(1, runs + 1)
    }


def radix(test_sizes: list, runs: int = 1) -> dict:
    """Run test_timer against radix_sort n times, given n = len(test_sizes) == len(input_sets)"""
    input_sets = read_test_input_files(path=Path(__file__).parent, test_input_sizes=test_sizes)
    return {
        f"run{run}": run_timers(radix_sort.radix_sort, test_sizes, input_sets)
        for run in range(1, runs + 1)
    }
    # radix_runs = dict()
    # for run in range(1, runs + 1):
    #     radix_runs[f"run{run}"] = run_timers(radix_sort.radix_sort, test_sizes, input_sets)
    # return radix_runs


if __name__ == "__main__":
    # perform timing tests for reporting...

    """Bubble Sort time performance reporting"""
    # bubble_times = bubble([3, 4], 5) # 2 - 3 min
    # bubble_times = bubble([5], 1) # > 20 min (~53 min)
    # print(f"bubble_sort (keys are 10**key):\t{bubble_times}")

    """Insertion Sort time performance reporting"""
    # insert_times = insert([3, 4], 5) # ~ 1 min
    # insert_times = insert([5], 4) # 14 - 19 min
    # print(f"insertion_sort (keys are 10**key):\t{insert_times}")

    """Merge Sort time performance reporting"""
    merge_times = merge([3, 4, 5, 6], 5) # 1 - 2 min
    # merge_times = merge([7], 5) # 12 - 14 min
    print(f"merge_sort (keys are 10**key):\t{merge_times}")

    """Radix Sort time performance reporting"""
    radix_times = radix([3, 4, 5, 6], 5) # ~ 1 min
    # radix_times = radix([7], 5) # 8 - 9 min
    # print(f"radix_sort (keys are 10**key):\t{radix_times}")

    """Quick Sort time performance reporting"""
    quick_times = quick([3, 4, 5, 6], 5) # < 1 min
    # quick_times = quick([7], 5) # < 1 min
    print(f"quick_sort (keys are 10**key):\t{quick_times}")

