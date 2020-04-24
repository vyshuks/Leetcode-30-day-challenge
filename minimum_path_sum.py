# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

# Example:

# Input:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.

def min_path_sum(grid):
    if grid is None or len(grid) ==0:
        return 0

    row = len(grid)
    col = len(grid[0])
    dp = [[0 for _ in range(col)] for _ in range(row)]
    
    for i in range(row):
        for j in range(col):
            dp[i][j] += grid[i][j]
            
            if i >0 and j >0:
                dp[i][j] += min(dp[i][j-1], dp[i-1][j])
            elif i > 0:
                dp[i][j] += dp[i-1][j]
            elif j>0 :
                dp[i][j] += dp[i][j-1]
    
    return dp[row-1][col-1]


grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
print(min_path_sum(grid))