class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        A_l = len(A)
        jump = 0
        cur = 0
        next = 0
        for i in xrange(A_l):
            if cur >= A_l -1:
                return jump

            if A[i] + i > cur:
                next = max([A[i] + i, next])
            if i ==  cur:
                cur = next
                jump += 1


        return jump

if __name__ == "__main__":
    print Solution().jump([1,2])
    print Solution().jump([0])
    print Solution().jump([7,0,9,6,9,6,1,7,9,0,1,2,9,0,3])
