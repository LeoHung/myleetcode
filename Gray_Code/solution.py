class Solution:
    # @return a list of integers
    def grayCode(self, n):
        dp = {}
        for i in range(n+1):
            if i == 0:
                dp[i] = [0]
                continue
            if i == 1:
                dp[i] = [0, 1]
                continue
            dp[i] = [ v for v in dp[i -1] ]
            this_sig = 2 ** (i-1)
            for v in dp[i-1][::-1]:
                dp[i].append(v + this_sig)

        return dp[n]

if __name__ == "__main__":
    print Solution().grayCode(2)
