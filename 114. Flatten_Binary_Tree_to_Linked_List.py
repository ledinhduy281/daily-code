'''
Template to run on VSCode

'''

import collections
import itertools
import functools
import math
import string
import random
import bisect
import re
import operator
import heapq
import queue

from icecream import ic
from queue import PriorityQueue
from itertools import combinations, permutations
from functools import lru_cache
from collections import defaultdict
from collections import OrderedDict
from collections import deque
from collections import Counter
from typing import Optional
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Flattens a binary tree into a linked list in-place.

        Args:
            root: The root node of the binary tree.

        Returns:
            None, modifies the root node in-place.
        """

        def dfs(node):
            if not node:
                return None

            # Handle empty left subtree
            left_tail = dfs(node.left)

            # Handle empty right subtree
            right_tail = dfs(node.right)

            # Connect the nodes in the correct order
            if left_tail:
                left_tail.right = node.right  # Connect left subtree tail to current node
            else:
                left_tail = node  # If left subtree is empty, current node becomes the tail

            node.right = node.left
            node.left = None

            # Return the tail node of the flattened subtree
            return right_tail or left_tail

        dfs(root)

    def print_flattened_tree(self, root):
        current = root
        while current:
            print(current.val, end=" ")
            current = current.right

# Create two binary trees in the global scope
# Tree 1:
#     3
#    / \
#   5   1
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.right = TreeNode(6)

ic(Solution().flatten(root))
