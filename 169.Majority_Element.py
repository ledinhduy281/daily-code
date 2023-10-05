'''
169. Majority Element
Easy
Topics
Companies
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109

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
    def majorityElement(self, nums: List[int]) -> int:
        # Hash map
        # d = Counter(nums)
        # ans = None
        # for k, v in d.items():
        #     if v > len(nums)//2:
        #         ans = k
        #         break
        # return ans

        # Boyer-Moore Voting Algorithm
        ans, count = 0, 0
        for num in nums:
            if count == 0:
                ans = num
            count += (1 if num == ans else -1)
            
print(Solution().majorityElement(nums = [2,2,1,1,1,2,2]))