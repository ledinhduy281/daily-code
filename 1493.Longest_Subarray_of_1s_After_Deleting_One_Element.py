'''

Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.

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

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # if n == 1:
        #     return True
        # if n < 4:  
        #     return False
        # while n > 4:
        #     if n % 4 != 0:
        #         return False
        #     n = n // 4
        # return True
        if n > 0 and (n & (n - 1)) == 0:
        # Check if the power of two is at an odd position
            return n & 0x55555555 == n
        return False

ic(Solution().isPowerOfFour(n=16))
