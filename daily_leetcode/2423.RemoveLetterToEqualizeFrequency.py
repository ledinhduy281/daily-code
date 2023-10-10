'''
You are given a 0-indexed string word, consisting of lowercase English letters. 

You need to select one index and remove the letter at that index from word 
so that the frequency of every letter present in word is equal.

Return true if it is possible to remove one letter so that the frequency of all letters in word are equal, 
and false otherwise.

Note:

The frequency of a letter x is the number of times it occurs in the string.
You must remove exactly one letter and cannot chose to do nothing.

Example 1:

Input: word = "abcc"
Output: true
Explanation: Select index 3 and delete it: word becomes "abc" and each character has a frequency of 1.
Example 2:

Input: word = "aazz"
Output: false
Explanation: We must delete a character, so either the frequency of "a" is 1 and the frequency of "z" is 2, 
or vice versa. It is impossible to make all present letters have equal frequency.

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
    def equalFrequency(self, word: str) -> bool:
        cntr1 = Counter(word)

        # Case 1 example: aaaa
        if len(cntr1.values()) == 1:
            return True

        # Case 2 example: abcd
        if all(val == 1 for val in cntr1.values()):
            return True
        
        cntr2 = Counter(cntr1.values())
        if len(cntr2.values()) != 2:
            return False
        
        # Case 3 example: aaaabbbbcccccdddd
        item1, item2 = cntr2.items()
        if item1 > item2:
            item1, item2 = item2, item1
        if item2[0] - item1[0] == 1 and item2[1] == 1:
            return True
        
        # Case 4 example: aaaabbbbcdddd
        if item1 == (1, 1):
            return True
        
        return False

print(Solution().equalFrequency(word="abcc"))