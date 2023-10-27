'''
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.



For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

 

Example 1:


Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true
Example 2:


Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false
 

Constraints:

The number of nodes in each tree will be in the range [1, 200].
Both of the given trees will have values in the range [0, 200].

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

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Create two binary trees in the global scope
# Tree 1:
#     3
#    / \
#   5   1
tree1 = TreeNode(3)
tree1.left = TreeNode(5)
tree1.right = TreeNode(1)

# Tree 2:
#     3
#    / \
#   6   1
tree2 = TreeNode(3)
tree2.left = TreeNode(6)
tree2.right = TreeNode(1)

class Solution:
    def leafSimilar(self, root1, root2):
        def dfs(node):
            if node:
                if not node.left and not node.right:
                    yield node.val
                yield from dfs(node.left)
                yield from dfs(node.right)

        # Call the leafSimilar function on the two trees
        leaf_sequence1 = list(dfs(tree1))
        leaf_sequence2 = list(dfs(tree2))

        # Check if the leaf sequences are similar
        is_similar = leaf_sequence1 == leaf_sequence2

        return is_similar

# Create a Solution object
solution = Solution()

# Call the leafSimilar function with the two trees
result = solution.leafSimilar(tree1, tree2)
print("Are the leaf sequences similar?", result)
