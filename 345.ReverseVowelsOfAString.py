'''

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.

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
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        s = list(s)
        start, end = 0, len(s) - 1

        while (start < end):
            while (start < len(s) and s[start] not in vowels):
                start += 1
            
            while (end >= 0 and s[end] not in vowels):
                end -= 1

            if (start < end):
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1

        return ''.join(s)
        

print(Solution().reverseVowels(s="hello"))