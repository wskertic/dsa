# Binary Search Trees

### Task 1: BST Class Implementation
_Define a class named ```BinarySearchTree``` with the following methods:_

- ```insert(self, value)```: Add an element to the tree.
- ```delete(self, value)```: Remove a node with the specified integer value from the tree.
- ```search(self, value)```: Find a specific element in the tree.
- ```in_order_traversal(self)```: display all elements in the tree in in-order(sorted order).
- ```pre_order_traversal(self)```: display all elements in the tree in pre-order.
- ```post_order_traversal(self)```: display all elements in the tree in post-order.
- ```height(self)```: Return the height of the tree.

### Task 2: BST Operations and Function Testing
_After implementing the ```BinarySearchTree``` class, test all its methods using a sequence of operations:_

#### Insertion and Basic Structure:
- Generate a list of 64 unique random integers within the range [1, 128].
- Insert each integer into the BST. After all insertions, print the tree's height.
#### Search Operations:
- Search for specific values (first, middle, and last in your list) in the BST. Print the outcome of each search.
#### Traversal Outputs:
- Print the results of the in-order, pre-order, and post-order traversals.
#### Deletion and Structure Adjustment:
- Delete specific values (first, middle, and last in your list) from the BST.
- After each deletion, print the tree's height and the in-order traversal.
#### Final Tree Height:
- Print the final height of the BST after all modifications.

### Task 3: Testing with Different Data Sets
_Conduct tests on multiple data sets to analyze the BST under different conditions:_

#### Varied Size Data Sets:
- *256 Integers*: Generate 256 unique random integers within [1, 512].
- *128 Integers*: Generate 128 unique random integers within [1, 256].
- *64 Integers*: Generate 64 unique random integers within [1, 128].

#### Worst-Case Scenario Test:
Use an ascending sequence (e.g., [1, 2, 3, ..., N]) to simulate the worst-case input and examine the tree's height and structure.
- Use an ascending sequence [1, 2, 3, ..., 64]
- Use an ascending sequence [1, 2, 3, ..., 128]
- Use an ascending sequence [1, 2, 3, ..., 256]

#### For each data set:
- Insert the numbers into a fresh BST instance.
- Print the in-order traversal results and the tree's height.
- *Optionally*, measure and compare the time taken for various operations.

### Task 4: Comparative Analysis and Discussions
- For each data set tested, including the worst-case scenario, note the tree height and summarize any structural changes.
- Write a discussion on the operational differences observed in the BST for average-case and worst-case inputs. Discuss any trends or behaviors in the height of the trees.