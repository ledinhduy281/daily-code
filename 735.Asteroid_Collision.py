'''
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

 

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
 

Constraints:

2 <= asteroids.length <= 104
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0

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
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            # Handle the case of the asteroid moving to the right
            if asteroid > 0:
                stack.append(asteroid)
            else:
                # Handle the case of the asteroid moving to the left
                while stack and stack[-1] > 0:
                    # Compare the sizes of the asteroids
                    if stack[-1] < abs(asteroid):
                        stack.pop()
                    elif stack[-1] == abs(asteroid):
                        stack.pop()
                        break
                    else:
                        break
                else:
                    stack.append(asteroid)

        return stack

ic(Solution().asteroidCollision(asteroids=[5,10,-5]))
