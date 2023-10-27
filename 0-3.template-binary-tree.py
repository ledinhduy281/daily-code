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

# Create two binary trees in the global scope
# Tree 1:
#     3
#    / \
#   5   1
tree1 = TreeNode(3)
tree1.left = TreeNode(5)
tree1.right = TreeNode(1)

# ic(Solution().())
