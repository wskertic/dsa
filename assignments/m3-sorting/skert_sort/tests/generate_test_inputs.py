#!/usr/bin/env python3

"""
Performance Testing: After implementing the sorting algorithms, assess their performance
using random data sets of 1,000, 10,000, 100,000, 1,000,000, and 10,000,000 integers
(ranging from 0 to 2,147,483,647). Ensure that the input data are unsorted and that all
algorithms use the identical input file for each input size. Note: If any algorithm takes
more than 20 minutes to sort data, terminate the program and denote this in your report as
"> 20 m".

One way to measure the execution time
# Start the timer
start_time = time.time()
# Run your algorithm
sample_algorithm()
# Stop the timer
end_time = time.time()
# Calculate the elapsed time
elapsed_time = end_time - start_time
"""

import array
import mmap
import struct
from pathlib import Path
from random import seed, randint


def create_random_int_set(e_size, seed_val="Camelot"):
    """Write a file with 10^e_size randomly generated integers (0 to 2,147,483,647)."""
    seed(seed_val)
    set_size = 10**e_size
    random_ints = array.array("l", range(set_size))
    for idx in range(set_size):
        random_ints[idx] = randint(0, 2147483647)
    random_ints = struct.pack(f"<{set_size}l", *random_ints)
    return random_ints


def write_test_file(path, content, max_length=0, force=False):
    """Write test file to test directory.

    Implementation from
    https://realpython.com/python-mmap/#writing-a-memory-mapped-file-with-pythons-mmap 05-Jun-24.
    https://www.askpython.com/python/examples/fastest-write-huge-data 05-Jun-24.
    """

    # content = bytes(content)
    try:
        with open(path, mode="x") as file_obj:
            file_obj.write("pythonpython")
    except FileExistsError as error:
        if force:
            pass
        else:
            raise FileExistsError("set force=True to overwrite existing file") from error
    with open(path, "w+b") as file_obj:
        with mmap.mmap(
            file_obj.fileno(), length=max_length, access=mmap.ACCESS_WRITE
        ) as mmap_obj:
            mmap_obj.write(content)
            mmap_obj.flush()


def generate_test_input_files(
    path, test_input_sizes: list = [3, 4, 5, 6, 7], force: bool = False
):
    """Execute test cases for task."""

    for size in test_input_sizes:
        packing_length = struct.calcsize(f"<{size}l")
        max_length = packing_length * 10**size
        try:
            write_test_file(
                path / f"random_int_set_e{size}.txt",
                create_random_int_set(size),
                max_length=max_length,
                force=force
            )
        except FileExistsError:
            raise


if __name__ == "__main__":
    current_directory = Path.cwd()
    generate_test_input_files(current_directory, [1])
