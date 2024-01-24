'''
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

Example 1:


Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:

Input: root = [1,null,3]
Output: [1,3]
Example 3:

Input: root = []
Output: []

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

# Create two binary trees in the global scope
# Tree 1:
#     3
#    / \
#   5   1
tree1 = TreeNode(3)
tree1.left = TreeNode(5)
tree1.right = TreeNode(1)

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def solve(root, lvl):
            if root:
                if len(res)==lvl:
                    res.append(root.val)
                solve(root.right, lvl + 1)
                solve(root.left, lvl + 1)
            return 

        res = []
        solve(root,0)
        return res

ic(Solution().rightSideView(root=tree1))
