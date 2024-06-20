#!/usr/bin/env python3

"""
Module Docstring

Insertion and Basic Structure:
- Generate a list of 64 unique random integers within the range [1, 128].
- Insert each integer into the BST. After all insertions, print the tree's height.
Search Operations:
- Search for specific values (first, middle, and last in your list) in the BST. Print the outcome of each search.
Traversal Outputs:
- Print the results of the in-order, pre-order, and post-order traversals.
Deletion and Structure Adjustment:
- Delete specific values (first, middle, and last in your list) from the BST.
- After each deletion, print the tree's height and the in-order traversal.
Final Tree Height:
- Print the final height of the BST after all modifications.


Conduct tests on multiple data sets to analyze the BST under different conditions:

Varied Size Data Sets:
- 256 Integers: Generate 256 unique random integers within [1, 512].
- 128 Integers: Generate 128 unique random integers within [1, 256].
- 64 Integers: Generate 64 unique random integers within [1, 128].
Worst-Case Scenario Test:
Use an ascending sequence (e.g., [1, 2, 3, ..., N]) to simulate the worst-case input and examine the tree's height and structure.
- Use an ascending sequence [1, 2, 3, ..., 64]
- Use an ascending sequence [1, 2, 3, ..., 128]
- Use an ascending sequence [1, 2, 3, ..., 256]
For each data set:
- Insert the numbers into a fresh BST instance.
- Print the in-order traversal results and the tree's height.
- Optionally, measure and compare the time taken for various operations.
"""

from random import randint, seed

from BinarySearchTree import BinarySearchTree as bst
# # from book_bst.linked_binary_tree import LinkedBinaryTree as bst
# from book_bst.tree_map import TreeMap as bst

seed("Camelot")
RANDOM_LARGE = [randint(1, 512) for _ in range(256)]
RANDOM_MEDIUM = [randint(1, 256) for _ in range(128)]
RANDOM_SMALL = [randint(1, 128) for _ in range(64)]

ASC_LARGE = [val for val in range(1, 256 + 1)]
ASC_MEDIUM = [val for val in range(1, 128 + 1)]
ASC_SMALL = [val for val in range(1, 64 + 1)]

test_inputs = {
    "RANDOM_LARGE": RANDOM_LARGE,
    "RANDOM_MEDIUM": RANDOM_MEDIUM,
    "RANDOM_SMALL": RANDOM_SMALL,
    "ASC_LARGE": ASC_LARGE,
    "ASC_MEDIUM": ASC_MEDIUM,
    "ASC_SMALL": ASC_SMALL,
}

print("\n\nASC means test set is in ascending order.")
for set_name, test_set in test_inputs.items():
    tree = bst()
    print(f"\nfor test set {set_name} with {len(test_set)} values")
    [tree.insert(val) for val in test_set]
    print(f"tree height: {tree.height()}")
    print("tree traversal: ")
    tree.in_order_traversal()
