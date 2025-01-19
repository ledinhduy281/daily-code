# class Solution:
#     # Class to store the height and coordinates of a cell in the grid
#     class Cell:
#         def __init__(self, height, row, col):
#             self.height = height
#             self.row = row
#             self.col = col

#         # Comparison method for the priority queue (min-heap)
#         def __lt__(self, other):
#             return self.height < other.height

#     # Helper function to check if a cell is valid (within grid bounds)
#     def _is_valid_cell(self, row, col, num_of_rows, num_of_cols):
#         return 0 <= row < num_of_rows and 0 <= col < num_of_cols

#     def trapRainWater(self, height_map):
#         # Direction arrays
#         d_row = [0, 0, -1, 1]
#         d_col = [-1, 1, 0, 0]

#         num_of_rows = len(height_map)
#         num_of_cols = len(height_map[0])

#         visited = [[False] * num_of_cols for _ in range(num_of_rows)]

#         # Priority queue (min-heap) to process boundary cells in increasing height order
#         boundary = []

#         # Add the first and last column cells to the boundary and mark them as visited
#         for i in range(num_of_rows):
#             heapq.heappush(boundary, self.Cell(height_map[i][0], i, 0))
#             heapq.heappush(
#                 boundary,
#                 self.Cell(height_map[i][num_of_cols - 1], i, num_of_cols - 1),
#             )
#             visited[i][0] = visited[i][num_of_cols - 1] = True

#         # Add the first and last row cells to the boundary and mark them as visited
#         for i in range(num_of_cols):
#             heapq.heappush(boundary, self.Cell(height_map[0][i], 0, i))
#             heapq.heappush(
#                 boundary,
#                 self.Cell(height_map[num_of_rows - 1][i], num_of_rows - 1, i),
#             )
#             visited[0][i] = visited[num_of_rows - 1][i] = True

#         # Initialize the total water volume to 0
#         total_water_volume = 0

#         # Process cells in the boundary (min-heap will always pop the smallest height)
#         while boundary:
#             # Pop the cell with the smallest height from the boundary
#             current_cell = heapq.heappop(boundary)

#             current_row = current_cell.row
#             current_col = current_cell.col
#             min_boundary_height = current_cell.height

#             # Explore all 4 neighboring cells
#             for direction in range(4):
#                 # Calculate the row and column of the neighbor
#                 neighbor_row = current_row + d_row[direction]
#                 neighbor_col = current_col + d_col[direction]

#                 # Check if the neighbor is within the grid bounds and not yet visited
#                 if (
#                     self._is_valid_cell(
#                         neighbor_row, neighbor_col, num_of_rows, num_of_cols
#                     )
#                     and not visited[neighbor_row][neighbor_col]
#                 ):
#                     # Get the height of the neighbor cell
#                     neighbor_height = height_map[neighbor_row][neighbor_col]

#                     # If the neighbor's height is less than the current boundary height, water can be trapped
#                     if neighbor_height < min_boundary_height:
#                         # Add the trapped water volume
#                         total_water_volume += (
#                             min_boundary_height - neighbor_height
#                         )

#                     # Push the neighbor into the boundary with updated height (to prevent water leakage)
#                     heapq.heappush(
#                         boundary,
#                         self.Cell(
#                             max(neighbor_height, min_boundary_height),
#                             neighbor_row,
#                             neighbor_col,
#                         ),
#                     )
#                     visited[neighbor_row][neighbor_col] = True

#         # Return the total amount of trapped water
#         return total_water_volume

import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        M = len(heightMap)
        N = len(heightMap[0])

        # Hint BFS
        h = []


        for i in [0, M-1]:
            for j in range(N):
                h.append((heightMap[i][j], i, j))
                heightMap[i][j] = -1

        for i in range(1, M-1):
            for j in [0, N-1]: 
                h.append((heightMap[i][j], i, j))
                heightMap[i][j] = -1

        heapq.heapify(h)
  

        tot = 0
        while h:
            height, x, y = heapq.heappop(h)
            stack = [(x,y)]
            while h and h[0][0] == height:
                _, x, y = heapq.heappop(h)
                stack.append((x,y))
            while stack:
                x, y  = stack.pop()
                for d in [-1,1]:
                    nX = x + d
                    nY = y + d
                    if 0 > nX or M <= nX or heightMap[nX][y] == -1:
                        pass
                    else:
                        if height > heightMap[nX][y]:
                            tot +=  height - heightMap[nX][y]
                            stack.append((nX, y))
                            heightMap[nX][y] = -1
                        else:
                            heapq.heappush(h, (heightMap[nX][y], nX, y))
                            heightMap[nX][y] = -1
                        
                    if 0 > nY or N <= nY or heightMap[x][nY] == -1:
                        pass
                    else:
                        if height > heightMap[x][nY]:
                            tot += height - heightMap[x][nY]
                            stack.append((x, nY))
                            heightMap[x][nY] = -1
                        else:
                            heapq.heappush(h, (heightMap[x][nY], x, nY))
                            heightMap[x][nY] = -1

        return tot