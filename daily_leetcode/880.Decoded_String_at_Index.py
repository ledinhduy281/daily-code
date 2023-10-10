'''
You are given an encoded string s. To decode the string to a tape, the encoded string is read one character at a time and the following steps are taken:

If the character read is a letter, that letter is written onto the tape.
If the character read is a digit d, the entire current tape is repeatedly written d - 1 more times in total.
Given an integer k, return the kth letter (1-indexed) in the decoded string.

 

Example 1:

Input: s = "leet2code3", k = 10
Output: "o"
Explanation: The decoded string is "leetleetcodeleetleetcodeleetleetcode".
The 10th letter in the string is "o".
Example 2:

Input: s = "ha22", k = 5
Output: "h"
Explanation: The decoded string is "hahahaha".
The 5th letter is "h".
Example 3:

Input: s = "a2345678999999999999999", k = 1
Output: "a"
Explanation: The decoded string is "a" repeated 8301530446056247680 times.
The 1st letter is "a".
 

Constraints:

2 <= s.length <= 100
s consists of lowercase English letters and digits 2 through 9.
s starts with a letter.
1 <= k <= 109
It is guaranteed that k is less than or equal to the length of the decoded string.
The decoded string is guaranteed to have less than 263 letters.

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
    def decodeAtIndex(self, s: str, k: int) -> str:
        # length = 0
        # i = 0
        
        # while length < k:
        #     if s[i].isdigit():
        #         length *= int(s[i])
        #     else:
        #         length += 1
        #     i += 1
        
        # for j in range(i-1, -1, -1):
        #     char = s[j]
        #     if char.isdigit():
        #         length //= int(char)
        #         k %= length
        #     else:
        #         if k == 0 or k == length:
        #             return char
        #         length -= 1
        total_length = 0
        for c in s:
            if c.isdigit():
                total_length *= int(c)
            else:
                total_length += 1
        for c in reversed(s):
            k %= total_length 
            if k == 0 and c.isalpha():
                return c
            if c.isdigit():
                total_length //= int(c)
            else:
                total_length -= 1
        return ""

print(Solution().decodeAtIndex(s = "ha22", k = 5))