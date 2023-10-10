'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.


Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]

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
    def moveZeroes(self, nums: List[int]) -> List:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
            # wait while we find a non-zero element to
            # swap with you
            if nums[slow] != 0:
                slow += 1
        return nums
                
        # anchor = 0
        # for explorer in range(len(nums)):
        #     if nums[explorer] != 0:
        #         nums[anchor], nums[explorer] = nums[explorer], nums[anchor]
        #         anchor += 1

print(Solution().moveZeroes(nums = [0,1,0,3,12]))