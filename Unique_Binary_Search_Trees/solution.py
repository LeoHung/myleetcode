class Solution:
    # @return an integer
    def numTrees(self, n):
        dp = {}
        for i in xrange(n+1):
            if i ==0 :
                dp[i] = 1
            elif i ==1 :
                dp[i] = 1
            elif i == 2:
                dp[i] = 2
            else:
                dp[i] = 0
                for j in xrange(i):
                    dp[i] += dp[j] * dp[i-j-1]

        return dp[n]
