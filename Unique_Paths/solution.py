class Solution:
    # @return an integer
    def stair(self, x):

        ret = 1
        for i in range(1, x+1):
            ret *= i
        return ret
    def uniquePaths(self, m, n):
        return self.stair(m +n -2) / (self.stair(m-1) * self.stair(n-1))
