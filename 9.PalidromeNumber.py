'''
Given an integer x, return true if x is a palindrome, and false otherwise.
'''
'''
Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.

The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.

The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.

Return an array of the k parts.

'''

from typing import List
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

        
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        
        reversedNum = 0

        while x > reversedNum:
            reversedNum = reversedNum * 10 + x % 10
            x //= 10
        return x == reversedNum or x == reversedNum // 10 
        


print(Solution().isPalindrome(x = 121))
print(Solution().isPalindrome(x = -121))
print(Solution().isPalindrome(x = 10)) 



        