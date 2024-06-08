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

# import array
import mmap
import struct
from os import PathLike
from pathlib import Path
from typing import List

try:
    from tests.generate_test_inputs import generate_test_input_files
except Exception:
    from generate_test_inputs import generate_test_input_files

def read_test_file(path: PathLike, max_length: int = None, force: bool = False):
    f"""Read test file from test directory.

    Parameters
    ----------
    path : pathlib.Path-like
        The location of the testfile to read as a bytes object from mmap
    max_length: numeric, optional
        Specifies the number of bytes to return from beginning of an mmap object
        {mmap.mmap.read.__doc__}
    force: bool, optional


    Returns
    -------
    mmap.read(max_length)
        A python bytes object of length max_length
    
    Implementation from
    https://realpython.com/python-mmap/#writing-a-memory-mapped-file-with-pythons-mmap 05-Jun-24.
    https://www.askpython.com/python/examples/fastest-write-huge-data 05-Jun-24.
    """

    try:
        with open(path, mode="rb") as file_obj:
            pass
    except FileNotFoundError as error:
        raise FileNotFoundError("set force=True to overwrite existing file") from error
    with open(path, "r+b") as file_obj:
        with mmap.mmap(
            file_obj.fileno(), length=0, access=mmap.ACCESS_WRITE
        ) as mmap_obj:
            return mmap_obj.read(max_length)


def read_test_input_files(
    path: PathLike = Path.cwd(),
    test_input_sizes: list = [3, 4, 5, 6, 7],
    create: bool = False,
) -> List[List[int]]: 
    """Execute test cases for task."""
    test_inputs = {}
    for size in test_input_sizes:
        test_file = path / f"random_int_set_e{size}.txt"
        if create:
            try:
                with open(test_file, mode="rb"):
                    print(f"found file {test_file}")
                    pass
            except FileNotFoundError:
                print(f"generating file {test_file}")
                generate_test_input_files(path, test_input_sizes)

        try:
            test_set = read_test_file(test_file, force=create)
            test_inputs[size] = struct.iter_unpack(f"<{size}l", test_set)
        except FileNotFoundError as error:
            raise FileNotFoundError(
                f"set create=True to generate new input of size 1e{size}"
            ) from error
    return [[val[0] for val in list(input_set)] for input_set in test_inputs.values()]


if __name__ == "__main__":
    current_directory = Path.cwd()
    input_sets = read_test_input_files(current_directory, [1, 3], create=False)
    print(input_sets[0][-5:])
