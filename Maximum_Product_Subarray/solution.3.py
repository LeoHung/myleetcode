class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        local_max = A[0]
        local_min = A[0]
        global_max = local_max
        for i in range(1, len(A)):
            tmp = [local_max * A[i], local_min * A[i], A[i]]

            local_max, local_min = max(tmp), min(tmp)
            global_max = max(local_max, global_max)

            print local_max, local_min

        return global_max


if __name__ == "__main__":
    print Solution().maxProduct([2,3,-2,4])
    print Solution().maxProduct([-2,0,-1])
    print Solution().maxProduct([-2])
    print Solution().maxProduct([7, -2, -4])
    print Solution().maxProduct([2,-5,-2,-4,3])
    print Solution().maxProduct([-1, -2, -9, -6])