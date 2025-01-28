# class Solution:
#     # Helper function to count the number of fishes in a connected component
#     def calculate_fishes(self, grid, visited, row, col):
#         # Check boundary conditions, water cells, or already visited cells
#         if (
#             row < 0
#             or row >= len(grid)
#             or col < 0
#             or col >= len(grid[0])
#             or grid[row][col] == 0
#             or visited[row][col]
#         ):
#             return 0

#         # Mark the current cell as visited
#         visited[row][col] = True

#         # Accumulate the fish count from the current cell and its neighbors
#         return (
#             grid[row][col]
#             + self.calculate_fishes(grid, visited, row, col + 1)
#             + self.calculate_fishes(grid, visited, row, col - 1)
#             + self.calculate_fishes(grid, visited, row + 1, col)
#             + self.calculate_fishes(grid, visited, row - 1, col)
#         )

#     def findMaxFish(self, grid):
#         rows, cols = len(grid), len(grid[0])
#         max_fish_count = 0

#         # A 2D list to track visited cells
#         visited = [[False] * cols for _ in range(rows)]

#         # Iterate through all cells in the grid
#         for row in range(rows):
#             for col in range(cols):
#                 # Start a DFS for unvisited land cells (fish available)
#                 if grid[row][col] > 0 and not visited[row][col]:
#                     max_fish_count = max(
#                         max_fish_count,
#                         self.calculate_fishes(grid, visited, row, col),
#                     )

#         # Return the maximum fish count found
#         return max_fish_count


class Solution:
    def dfs(self, grid, i, j):
        nrow, ncol = len(grid), len(grid[0])
        if i < 0 or j < 0 or i >= nrow or j >= ncol:
            return 0
        if grid[i][j] == 0:
            return 0
        temp = grid[i][j]
        grid[i][j] = 0
        return temp + self.dfs(grid, i+1, j) + self.dfs(grid, i-1, j) + self.dfs(grid, i, j+1) + self.dfs(grid, i, j-1)

    def findMaxFish(self, grid: List[List[int]]) -> int:
        res = 0
        nrow, ncol = len(grid), len(grid[0])
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] != 0:
                    res = max(res, self.dfs(grid, i, j))
        return res

        