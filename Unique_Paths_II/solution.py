class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        N = len(obstacleGrid)
        if N <= 0:
            return 0

        M = len(obstacleGrid[0])
        if M <= 0:
            return 0

        dp = {}
        for i in range(N):
            for j in range(M):
                if obstacleGrid[i][j] == 1:
                    dp[(i,j)] = 0
                    continue

                if i == 0 and j ==0:
                    dp[(i, j)] = 1
                elif i == 0:
                    dp[(i, j)] = dp[(i, j-1)]
                elif j == 0:
                    dp[(i, j)] = dp[(i-1, j)]
                else:
                    dp[(i,j)] = dp[(i-1,j)] + dp[(i,j-1)]
        return dp[(N-1,M-1)]

