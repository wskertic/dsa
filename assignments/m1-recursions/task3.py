#!/usr/bin/env python3

"""
Task 3 description

Write a recursive function that reverses a string.
The function should take a string as input and return the reversed string as output.

For example,
if the input is "Hello World", the output should be "dlroW olleH".
"""


def reverse_recurse(input: str) -> str:
    """Recursive implementation of string reversal."""
    if input:
        return input[-1] + reverse_recurse(input[:-1])
    return str()


def test():
    test_cases = {
        ".+": "+.",
        "Hello World": "dlroW olleH",
        "0": "0",
        "deified": "deified",
        """\nIt is I, Arthur, son of Uther Pendragon,
from the castle of Camelot. King of the Britons,
defeater of the Saxons, Sovereign of all England!
        """: """\t\n!dnalgnE lla fo ngierevoS ,snoxaS eht fo retaefed 
,snotirB eht fo gniK .tolemaC fo eltsac eht morf
,nogardneP rehtU fo nos ,ruhtrA ,I si tI""",
        #   5: TypeError,
        #   True: TypeError
    }

    print(f"\n{__file__[-8:-3]}\n-----------------------------\n")
    [
        print(
            f"\n       for input: {k}\nfunction returns: {reverse_recurse(k)}\n   correct value: {v}"
        )
        for k, v in test_cases.items()
    ]


if __name__ == "__main__":
    test()
