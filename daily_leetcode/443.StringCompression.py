'''

Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.

Otherwise, append the character followed by the group's length.

The compressed string s should not be returned separately, 
but instead, be stored in the input character array chars. 

Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.


Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
Example 2:

Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.
Example 3:

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".


Constraints:

1 <= chars.length <= 2000
chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.

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
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0

        write_idx = 0  # Index to write compressed characters
        count = 1  # Initialize the count of consecutive characters

        for i in range(1, len(chars)):
            if chars[i] == chars[i - 1]:
                count += 1
            else:
                chars[write_idx] = chars[i - 1]  # Write the character

                if count > 1:
                    count_str = str(count)
                    chars[write_idx + 1:write_idx + 1 + len(count_str)] = count_str  # Write the count as characters
                    write_idx += len(count_str)

                write_idx += 1  # Move the write index to the next position
                count = 1  # Reset the count

        # Write the last character and count if needed
        chars[write_idx] = chars[-1]
        if count > 1:
            count_str = str(count)
            chars[write_idx + 1:write_idx + 1 + len(count_str)] = count_str
            write_idx += len(count_str)

        return write_idx + 1  # Return the new length of the array

print(Solution().compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))