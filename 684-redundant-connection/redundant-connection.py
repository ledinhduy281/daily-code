# class Solution:
#     # Performs DFS and returns True if there's a path between src and target.
#     def _is_connected(self, src, target, visited, adj_list):
#         visited[src] = True

#         if src == target:
#             return True

#         is_found = False
#         for adj in adj_list[src]:
#             if not visited[adj]:
#                 is_found = is_found or self._is_connected(
#                     adj, target, visited, adj_list
#                 )

#         return is_found

#     def findRedundantConnection(self, edges):
#         N = len(edges)

#         adj_list = [[] for _ in range(N)]

#         for edge in edges:
#             visited = [False] * N

#             # If DFS returns True, we will return the edge.
#             if self._is_connected(edge[0] - 1, edge[1] - 1, visited, adj_list):
#                 return edge

#             adj_list[edge[0] - 1].append(edge[1] - 1)
#             adj_list[edge[1] - 1].append(edge[0] - 1)

#         return []

# Union-find, Time O(V + E), Space O(V)
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Define parent and rank array
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        # Define find & union
        def find(n):
            if n != par[n]:
                par[n] = find(par[n])
            return par[n]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            # Already connected
            if p1 == p2:
                return False
            # Connect
            if rank[p1] >= rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True

        # Find redundant edge
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]