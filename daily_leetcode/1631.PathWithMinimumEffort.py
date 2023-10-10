'''


You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.

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
import heapq as hq
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
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        
        pq = [(0, 0, 0)] 
        
        while pq:
            effort, x, y = hq.heappop(pq)
            if (x, y) in visited:
                continue
            visited.add((x, y))
            if (x, y) == (rows - 1, cols - 1):
                return effort
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                    new_effort = max(effort, abs(heights[x][y] - heights[nx][ny]))
                    hq.heappush(pq, (new_effort, nx, ny))

        # rows, cols = len(heights), len(heights[0])
        # directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # dist = [[math.inf for _ in range(cols)] for _ in range(rows)]
        # dist[0][0] = 0
        # minHeap = [(0, 0, 0)] 
        
        # while minHeap:
        #     effort, x, y = hq.heappop(minHeap)

        #     if x == rows - 1 and y == cols - 1:
        #         return effort
            
        #     for dx, dy in directions:
        #         nx, ny = x + dx, y + dy
                
        #         if 0 <= nx < rows and 0 <= ny < cols:
        #             new_effort = max(effort, abs(heights[x][y] - heights[nx][ny]))
                    
        #             if new_effort < dist[nx][ny]:
        #                 dist[nx][ny] = new_effort
        #                 hq.heappush(minHeap, (new_effort, nx, ny))

print(Solution().minimumEffortPath(heights=[[1,2,2],[3,8,2],[5,3,5]]))