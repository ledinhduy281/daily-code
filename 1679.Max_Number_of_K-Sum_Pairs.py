'''
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.


Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
Example 2:

Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= k <= 109

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
    def maxOperations(self, nums: List[int], k: int) -> int:
        #Approach 1: Hash Map
        # Initialize a result variable to count the maximum number of pairs.
        res = 0
        
        # Use a Counter to count the occurrences of each number in nums.
        d = Counter(nums)
        
        # Iterate through the unique values in the input.
        for val1 in d.keys():
            # Calculate the complementary value needed to reach k.
            val2 = k - val1
            
            # Check if val2 is less than val1 (to avoid duplicates) or if val2 is not in the counter.
            if val2 < val1 or val2 not in d:
                continue
            
            # If val1 is equal to val2, it means we have duplicate values.
            # In this case, we can form d[val1] // 2 pairs because we need two instances of the same value.
            if val1 == val2:
                res += d[val1] // 2
            else:
                # Otherwise, we can form a minimum number of pairs equal to the minimum count
                # of val1 and val2 in the input.
                res += min(d[val1], d[val2])
        
        # Return the maximum number of pairs that sum up to k.
        return res

        # Approach 2: Two Pointers
        # count, left, right = 0, 0, len(nums) - 1
        # nums.sort()
        # while (left < right):
        #     curr = nums[left] + nums[right]
        #     if (curr == k):
        #         count += 1
        #         left += 1  
        #         right -= 1
        #     elif (curr < k):
        #         left += 1  
        #     else:
        #         right -= 1
        # return count


print(Solution().maxOperations(nums = [1,2,3,4,6,6,11,9,10], k = 12))