class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        ways = [ 0 for i in range(n) ]
        for i in range(n):
            if i == 0:
                ways[i] = 1
            elif i == 1:
                ways[i] = 2
            else:
                ways[i] = ways[i-1] + ways[i-2]

        return ways[-1]

