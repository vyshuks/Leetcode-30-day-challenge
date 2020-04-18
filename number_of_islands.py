# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input:
# 11110
# 11010
# 11000
# 00000

# Output: 1
# Example 2:

# Input:
# 11000
# 11000
# 00100
# 00011

# Output: 3


def bfs(grid, i, j):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] == '0':
        return 0
    grid[i][j] = '0'
    bfs(grid,i,j+1)
    bfs(grid, i, j-1)
    bfs(grid,i-1, j)
    bfs(grid, i+1, j)
    return 1

def numIslands(grid):
    if grid is None or len(grid)==0:
        return 0

    num_islands = 0
    for i  in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                num_islands += bfs(grid, i, j)
    
    return num_islands



graph = [['1', '1', '0', '0', '0'], 
        ['1', '1', '0', '0', '0'], 
        ['0', '0', '1', '0', '0'], 
        ['0', '0', '0', '1', '1'], 
        ] 

print(numIslands(graph))