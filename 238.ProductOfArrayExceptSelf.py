'''

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer

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

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # Khởi tạo mảng kết quả với tất cả giá trị là 1
        result = [1] * n
        
        # Tính tích của các phần tử bên trái và lưu trực tiếp vào mảng kết quả
        left_product = 1
        for i in range(n):
            result[i] *= left_product
            left_product *= nums[i]
        
        # Tính tích của các phần tử bên phải và cập nhật mảng kết quả
        right_product = 1
        for i in range(n - 1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]
        
        return result

print(Solution().productExceptSelf(nums = [1, 2, 3, 4]))