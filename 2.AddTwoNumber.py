'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list. 
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

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
    def add_nodes(self, parent, vals):
        while len(vals) > 0:
            node = ListNode(vals[0])
            parent.next = node
            return self.add_nodes(node, vals[1:])

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0
        
        while l1 or l2 or carry:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            columnSum = l1Val + l2Val + carry
            carry = columnSum // 10
            newNode = ListNode(columnSum % 10)
            curr.next = newNode
            curr = newNode
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummyHead.next

# Create the input linked lists
# l1 = 2 -> 4 -> 3
l1 = ListNode(2, ListNode(4, ListNode(3)))
# l2 = 5 -> 6 -> 4
l2 = ListNode(5, ListNode(6, ListNode(4)))

result = Solution().addTwoNumbers(l1, l2)

# Print the result as a list (in reverse order)
while result:
    print(result.val, end=" -> ")
    result = result.next
