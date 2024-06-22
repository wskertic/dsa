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


def gen_unique_rands(number, range_max, start=1):
    """Ensure a unique set of integers is generated"""
    # if start is not None:
    #     range_max, start = start, range_max
    # else:
    #     start = 1
    existing = [None for _ in range(number)]
    for idx in range(number):
        rando = randint(start, range_max)
        while rando in set(existing):  # check if number already in the list
            rando = randint(start, range_max)  # find a number not yet in the list
        existing[idx] = rando
    return existing


seed("Camelot")
RANDOM_LARGE = gen_unique_rands(256, 512)
seed("Camelot")
RANDOM_MEDIUM = gen_unique_rands(128, 256)
seed("Camelot")
RANDOM_SMALL = gen_unique_rands(64, 128)

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

tree = bst()
start = test_inputs["RANDOM_SMALL"][0]
mid = test_inputs["RANDOM_SMALL"][
    (small_inputs := len(test_inputs["RANDOM_SMALL"])) // 2
]
end = test_inputs["RANDOM_SMALL"][-1]

[tree.insert(val) for val in test_inputs["RANDOM_SMALL"]]
print(f"\n\n{'-'*24} Task 2 {'-'*24}\n")
print(
    f"Tree heigh after inserting {small_inputs} values:  {tree.height()}",
    f"\nSearching for first value inserted, {start}:  {tree.search(start)}",
    f"\nSearching for middle value inserted, {mid}:  {tree.search(mid)}",
    f"\nSearching for last value inserted, {end}:  {tree.search(end)}",
    "\n\nPrinting tree traversals for in-order, pre-order, and post-order traversals: ...\n",
)
tree.in_order_traversal()
tree.pre_order_traversal()
tree.post_order_traversal()

print(
    f"\n\nPrior to deleting any values, the tree height is {tree.height()}",
    f"\nDeleting the first value inserted, {start}, deleted successfully:  {tree.delete(start)}\n",
    f"After deleting the first value the new tree height is {tree.height()} and traversal",
)
tree.in_order_traversal()
print(
    f"\nDeleting the middle value inserted, {mid}, deleted successfully:  {tree.delete(mid)}\n",
    f"After deleting the middle value the new tree height is {tree.height()} and traversal",
)
tree.in_order_traversal()
print(
    f"\nDeleting the last value inserted, {end}, deleted successfully:  {tree.delete(end)}\n",
    f"After deleting the last value the new tree height is {tree.height()} and traversal",
)
tree.in_order_traversal()


print(f"\n\n{'-'*24} Task 3 {'-'*24}\n")
print(
    "ASC means test set is in ascending order,",
    "i.e.\nASC_MEDIUM is an ascending sequence [1, 2, 3, ..., 128].",
)
for set_name, test_set in test_inputs.items():
    tree = bst()
    print(f"\nfor test set {set_name} with {len(test_set)} values")
    [tree.insert(val) for val in test_set]
    print(f"tree height: {tree.height()}")
    print("tree traversal: ")
    tree.in_order_traversal()
