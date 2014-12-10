class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        dp = {}
        N = len(grid)
        M = len(grid[0])
        for i in range(N):
            for j in range(M):
                if i == 0 and j == 0:
                    dp[(i,j)] = grid[i][j]
                elif i == 0:
                    dp[(i,j)] = grid[i][j] + dp[(i,j-1)]
                elif j == 0:
                    dp[(i,j)] = grid[i][j] + dp[(i-1,j)]
                else:
                    dp[(i,j)] = grid[i][j] + min( [ dp[(i,j-1)], dp[(i-1,j)] ])
        return dp[ (N-1, M-1)]
