#!/usr/bin/env python3

"""Module Docstring"""

import re


class HashTable:
    """Class Docstring"""

    def __init__(self):
        self.size = 10
        self.table = [-1 for key in range(self.size)]
        self.index = [idx for idx in range(self.size)]
        self.TASK_KEYS = [15, 27, 5, 12, 35]
        self.is_full = False

    def print_table(self):
        self.__table_idx = [f"{idx: 3d}" for idx in self.index]
        self.__table_vals = [f"{val: 3d}" for val in self.table]
        self.__table_idx = re.sub(
            r"[\[,\]]", "|", str(self.__table_idx).replace("'", "")
        )
        self.__table_vals = re.sub(
            r"[\[,\]]", "|", str(self.__table_vals).replace("'", "")
        )
        print()
        print("Index", self.__table_idx)
        print("Value", self.__table_vals)
        print()

    def hash_function(self, key, iteration):
        return (key + iteration**3) % 10

    def insert(self, key):
        """Insert key into next available slot.

        Attempt to insert key into hash_function(key, iteration) hash table index.
        If there is already a key at that index,
            i.e. collision, use a linear probing approach to open addressing.
        If the table becomes full, return an appropriate message.
        """
        # linear probe approach to open addressing
        if self.is_full:
            print("Hash Table is already full.")
            return False
        # for loop enables potentially visiting every hash table index once
        for iteration in range(10):  # will only run once if no collisions
            try_index = self.hash_function(key, iteration)

            if self.table[try_index] == -1:  # if no collision, key will insert
                self.table[try_index] = key  # insert key in free index
                print(
                    f"No collision -- succesfully inserted key {key}",
                    f"at hash table index {try_index}",
                )
                self.print_table()
                return True  # returns a successful status for insert operation
            else:
                print(
                    f"Key collision for key {key}",
                    f"index {try_index} -- linear probe next open address",
                )
        self.is_full = True  # only runs if all indices produce collisions
        print("Hash Table is already full.")
        return False  # returns an unsuccessful status for insert operation

    def run_test(self, keys=None):
        if not keys:
            keys = self.TASK_KEYS
        print(f"\nAttempting to insert keys from {keys} into hash table...\n")
        [self.insert(key) for key in keys]


if __name__ == "__main__":
    HashTable().run_test()
    # HashTable().run_test([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
