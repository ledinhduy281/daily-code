'''
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

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

from queue import PriorityQueue
from itertools import combinations, permutations
from functools import lru_cache
from collections import defaultdict
from collections import OrderedDict
from collections import deque
from collections import Counter
from typing import Optional
from typing import List

class Solution:
    def addDigits(self, num: int) -> int:
        # return (num - 1)%9 + 1 if num else 0
        return num % 9 or (num and 9)


print(Solution().addDigits(num=0))
print(Solution().addDigits(num=38))