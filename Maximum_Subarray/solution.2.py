class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        cur = 0
        max_ret = max(A)


        for e in A:
            cur += e

            if cur < 0:
                cur = 0

            if e > 0 and cur > 0:
                max_ret = max([cur, max_ret])

        return max_ret
