#!/usr/bin/env python3

"""
Timer for assessing sorting algorithm performance.

Provided in project description on instructure:
https://iu.instructure.com/courses/2241451/assignments/16139106?module_item_id=32343461
"""

import time


def test_timer(function, input):
    """Run function inside a timing framework to return elapsed run time."""

    start_time = time.perf_counter()
    function(input)
    end_time = time.perf_counter()
    run_time = f"{end_time - start_time}"
    return run_time

if __name__ == '__main__':
        print(test_timer(time.sleep, 5))
