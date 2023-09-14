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

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length, current, parts = 0, head, []
        
        while current:
            length += 1
            current = current.next
        
        base_size, extra = divmod(length, k)
        current = head
        
        for _ in range(k):
            dummy = ListNode()
            part_head = dummy
            
            for _ in range(base_size + (extra > 0)):
                dummy.next, current, dummy = current, current.next, current
            
            if extra > 0:
                extra -= 1
            dummy.next = None
            parts.append(part_head.next)
        
        return parts


# Create the input linked list from a list
head = ListNode(1, ListNode(2, ListNode(3)))
result = Solution().splitListToParts(head, 2)

# Print the results
for part in result:
    current = part
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print(None)  # Print None to represent the end of a part



        