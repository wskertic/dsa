#!/usr/bin/env python3

"""Binary Search Tree

Implementation from Joey James.
https://github.com/joeyajames/Python/blob/master/Trees/BinarySearchTree.py accessed 12-Jun-24.
"""


class BinarySearchTree:
    """Facilitates structure and function of trees using nodes.
    Attributes
    ----------
    height
    max
    min

    Methods
    -------
    insert
    delete
    search
    in_order_traversal
    pre_order
    post_order
    get_depth
    get_max
    get_min
    is_root
    print_tree
    """

    def __init__(self):
        self.root = None

    def insert(self, data):
        """handles 2 cases:
        1. root node exists - > insert
        2. root node does not exist - > create
        """

        if self.root:
            # print(f"about to call insert({data}) on root node...")
            return self.root.insert(data)
        else:
            # print(f"about to create new root node with {data}...")
            self.root = BinarySearchTree.Node(data)
            return True

    def delete(self, data):  # I hate this implementation
        """handles 4 cases:
        1. data does not exist - > error or false
        2. data in leaf or root - > set to None
        3. data has 1 child - > swap, then set to None
        4. data has 2 childdren - > find next largest (go right, *left), swap, then set to None
        """

        # empty tree
        if self.root is None:
            return False

        # data is in root node #TODO: ❌ there's an error here, results in duplicate data in tree
        elif self.root.value == data:
            if self.root.left_child is None and self.root.right_child is None:
                self.root = None
            elif self.root.left_child and self.root.right_child is None:
                self.root = self.root.left_child
            elif self.root.left_child is None and self.root.right_child:
                self.root = self.root.right_child
            elif self.root.left_child and self.root.right_child:
                del_node_parent = self.root
                del_node = self.root.right_child
                while del_node.left_child:
                    del_node_parent = del_node
                    del_node = del_node.left_child

                if del_node.right_child:
                    if del_node_parent.value > del_node.value:
                        del_node_parent.left_child = del_node.right_child
                    elif del_node_parent.value < del_node.value:
                        del_node_parent.right_child = del_node.right_child
                else:
                    if del_node.value < del_node_parent.value:
                        del_node_parent.left_child = None
                    else:
                        del_node_parent.right_child = None
                self.root.value = del_node.value

                return True

        parent = None
        node = self.root
        # need to find data node to remove
        while node and node.value != data:
            parent = node
            if data < node.value:
                node = node.left_child
            elif data > node.value:
                node = node.right_child

        # case 1: data not found
        if node is None or node.value != data:
            return False

        # case 2: remove-node has no children
        elif node.left_child is None and node.right_child is None:
            if data < parent.value:
                parent.left_child = None
            else:
                parent.right_child = None
            return True

        # case 3: remove-node has left child only
        elif node.left_child and node.right_child is None:
            if data < parent.value:
                parent.left_child = node.left_child
            else:
                parent.right_child = node.left_child
            return True

        # case 4: remove-node has right child only
        elif node.left_child is None and node.right_child:
            if data < parent.value:
                parent.left_child = node.right_child
            else:
                parent.right_child = node.right_child
            return True

        # case 5: remove-node has left and right children
        else:
            del_node_parent = node
            del_node = node.right_child
            while del_node.left_child:
                del_node_parent = del_node
                del_node = del_node.left_child

            node.value = del_node.value
            if del_node.right_child:
                if del_node_parent.value > del_node.value:
                    del_node_parent.left_child = del_node.right_child
                elif del_node_parent.value < del_node.value:
                    del_node_parent.right_child = del_node.right_child
            else:
                if del_node.value < del_node_parent.value:
                    del_node_parent.left_child = None
                else:
                    del_node_parent.right_child = None

    def search(self, data):  # returns Node object
        """handles 2 cases:
        1. root exists - > find data from root
        2. root does not exist - > error or false
        """

        if self.root:
            return self.root.search(data)
        else:
            return False

    def in_order_traversal(self):
        """Traverses tree using the in-order strategy.

        in-order strategy is max left child, node, right child through root, to max right child
        """

        if self.root is not None:
            print("in-order")
            self.root.in_order_traversal()

    def pre_order_traversal(self):
        """Traverses tree using the pre-order strategy.

        pre-order strategy is node, left child, right child, through max left child to max right child
        """

        if self.root is not None:
            print("pre-order")
            self.root.pre_order_traversal()

    def post_order_traversal(self):
        """Traverses tree using the post-order strategy.

        post-order strategy is left child, right child, node, through max left child to max right child
        """

        if self.root is not None:
            print("post-order")
            self.root.post_order_traversal()

    def height(self, data=None):  # TODO: this is just wrong 🤦
        """Measures the height of data"""

        # if data is None:
        #     return self.max_depth()
        # else:
        #     return self.height(self.data)

        if self.root:
            return self.root.height() - 1
        else:
            return -1

    class Node:
        """Facilitates structure and function of nodes for use in trees.

        Attributes
        ----------
        value
        left_child
        right_child
        depth

        Methods
        -------
        insert
        search
        in_order_traversal
        pre_order
        post_order
        get_height
        """

        def __init__(self, value):
            self.value = value
            self.left_child = None
            self.right_child = None

        def children(self):
            """Returns dictionary of child objects."""
            return {"left_child": self.left_child, "right_child": self.right_child}

        def insert(self, data):
            """Insert data into appropriate node of tree.

            Handles 3 cases:
            1. data is already in parent node
            2. data is less than parent node
            3. data is greater than parent node

            Handles 2 sub-cases:
            1. appropriate child node already exists
            2. appropriate child node must be created
            """

            if data == self.value:
                return False

            elif data < self.value:
                if self.left_child:
                    return self.left_child.insert(data)
                else:
                    self.left_child = BinarySearchTree.Node(data)
                    return True
            else:
                if self.right_child:
                    return self.right_child.insert(data)
                else:
                    self.right_child = BinarySearchTree.Node(data)
                    return True

        def search(self, data):
            """ """

            if data == self.value:
                return True
            elif data < self.value:
                if self.left_child:
                    return self.left_child.search(data)
                else:
                    return False
            else:
                if self.right_child:
                    return self.right_child.search(data)
                else:
                    return False

        def height(self):
            """handles 3 cases:
            1. leaf node
            2. 1 child
            3. 2 children
            """

            if self.left_child and self.right_child:  # 2 children
                return 1 + max(self.left_child.height(), self.right_child.height())
            elif self.left_child:
                return 1 + self.left_child.height()
            elif self.right_child:
                return 1 + self.right_child.height()
            else:  # leaf node
                return 1

        def in_order_traversal(self):
            """Traverses tree using the in-order strategy.

            in-order strategy is max left child, node, right child through root, to max right child
            """

            if self:
                if self.left_child:
                    self.left_child.in_order_traversal()
                print(str(self.value))
                if self.right_child:
                    self.right_child.in_order_traversal()

        def pre_order_traversal(self):
            """Traverses tree using the pre-order strategy.

            pre-order strategy is node, left child, right child, through max left child to max right child
            """

            if self:
                print(str(self.value))
                if self.left_child:
                    self.left_child.pre_order_traversal()
                if self.right_child:
                    self.right_child.pre_order_traversal()

        def post_order_traversal(self):
            """Traverses tree using the post-order strategy.

            post-order strategy is left child, right child, node, through max left child to max right child
            """

            if self:
                if self.left_child:
                    self.left_child.post_order_traversal()
                if self.right_child:
                    self.right_child.post_order_traversal()
                print(str(self.value))


if __name__ == "__main__":
    test_sequence = [5, 3, 7, 9, 1, 17, 19, 15, 2, 4, 6, 10, 18, 12, 13]
    remove_sequence = [19, 18, 17, 15, 13, 12]
    tree = BinarySearchTree()
    [print(tree.insert(val)) for val in test_sequence]
    tree.in_order_traversal()
    tree.pre_order_traversal()
    print(f"height: {tree.height()}")
    print(tree.delete(5))
    tree.in_order_traversal()
    tree.pre_order_traversal()
    print(tree.delete(6))
    tree.in_order_traversal()
    tree.pre_order_traversal()
    print([tree.delete(val) for val in remove_sequence])
    tree.in_order_traversal()
    print(f"height: {tree.height()}")

    tree1 = BinarySearchTree()
    print(f"empty tree height: {tree1.height()}")
    [tree1.insert(val) for val in range(1, 4)]
    print(f"ascending 3 node tree height {tree1.height()}")
