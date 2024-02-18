'''
Template to run on VSCode

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
from numpy import inf

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        room_available = [0] * n
        meeting_count = [0] * n
        for start, end in sorted(meetings):
            min_time_available = inf
            min_available_time_room = 0
            found_available_room = False
            for i in range(n):
                if room_available[i] <= start:
                    room_available[i] = end
                    meeting_count[i] += 1
                    found_available_room = True
                    break
                if room_available[i] < min_time_available:
                    min_time_available = room_available[i]
                    min_available_time_room = i
            if not found_available_room:
                room_available[min_available_time_room] += end-start
                meeting_count[min_available_time_room] += 1
                
        return meeting_count.index(max(meeting_count))

ic(Solution().mostBooked(n = 3, meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]))
