'''
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

    1    
   1 1   
  1 2 1  
 1 3 3 1 
1 4 6 4 1


Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]

Constraints:

1 <= numRows <= 30

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
    def generate(self, numRows: int) -> List[List[int]]:
        # import math
        # triangle = []
        # for n in range(numRows):
        #     row = []
        #     for k in range(n+1):
        #         row.append(math.comb(n, k))
        #     triangle.append(row)
        
        # return triangle
        
        res = [[1]]
        for i in range(numRows - 1):
            ans = [0] + res[-1] + [0]
            row = []
            for j in range(len(res[-1]) + 1):
                row.append(ans[j] + ans[j + 1])
            res.append(row)
        return res
        

print(Solution().generate(numRows=5))