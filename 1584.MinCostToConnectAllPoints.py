'''
Medium

You are given an array points representing integer coordinates of some points on a 2D-plane, 
where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, 
where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. 

All points are connected if there is exactly one simple path between any two points.

Example:

Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18

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

def manhattan_distance(p1: List[int], p2: List[int]) -> int:
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        
    def find(self, u):
        if self.parent[u] == u:
            return u
        self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)
        
        if u == v:
            return False
        
        if self.rank[u] > self.rank[v]:
            u, v = v, u
            
        self.parent[u] = v
        
        if self.rank[u] == self.rank[v]:
            self.rank[v] += 1
        
        return True


class Solution:
    # Prim algorithm
    
    # def minCostConnectPoints(self, points: List[List[int]]) -> int:
    #     n = len(points)
    #     visited = [False] * n
    #     heap_dict = {0: 0}  
    #     min_heap = [(0, 0)]
        
    #     mst_weight = 0
        
    #     while min_heap:
    #         w, u = hq.heappop(min_heap)
            
    #         if visited[u] or heap_dict.get(u, float('inf')) < w:
    #             continue
            
    #         visited[u] = True
    #         mst_weight += w
            
    #         for v in range(n):
    #             if not visited[v]:
    #                 new_distance = manhattan_distance(points[u], points[v])
    #                 if new_distance < heap_dict.get(v, float('inf')):
    #                     heap_dict[v] = new_distance
    #                     hq.heappush(min_heap, (new_distance, v))   
    #     return mst_weight

    # Kruskal algorithm
    
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        uf = UnionFind(n)
        
        edges = []
        
        for i in range(n):
            for j in range(i+1, n):
                distance = manhattan_distance(points[i], points[j])
                hq.heappush(edges, (distance, i, j))
        
        mst_weight = 0
        mst_edges = 0
        
        while edges:
            w, u, v = hq.heappop(edges)
            if uf.union(u, v):
                mst_weight += w
                mst_edges += 1
                if mst_edges == n - 1:
                    break
                    
        return mst_weight
        
print(Solution().minCostConnectPoints(points=[[0,0],[2,2],[3,10],[5,2],[7,0]]))
print(Solution().minCostConnectPoints(points=[[3,12],[-2,5],[-4,1]]))