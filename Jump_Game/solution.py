class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        A_l = len(A)

        cur_max = 0
        for i in xrange(A_l):
            if i > cur_max:
                return False
            if cur_max >= A_l -1:
                return True
            cur_max = max([cur_max, A[i] + i ])

        return cur_max >= A_l -1
