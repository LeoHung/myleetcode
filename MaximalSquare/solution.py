class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare(self, matrix):
        if matrix == None:
            return 0

        N = len(matrix)
        if N > 0:
            M = len(matrix[0])
        else:
            return 0

        cache = [[0 for j in xrange(M)] for i in xrange(N)]

        max_value = 0

        for i in xrange(N):
            for j in xrange(M):
                if matrix[i][j] == '0':
                    cache[i][j] = 0
                else:
                    if i > 0 and j > 0:
                        if cache[i-1][j] > 0 and cache[i][j-1] > 0 and cache[i-1][j-1] > 0:
                            cache[i][j] = min([cache[i-1][j], cache[i][j-1], cache[i-1][j-1]]) + 1
                        else:
                            cache[i][j] = 1
                    else:
                        cache[i][j] = 1
                    max_value = max([cache[i][j], max_value])

        return max_value * max_value
