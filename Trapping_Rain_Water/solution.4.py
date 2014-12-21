class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        left = [ 0 for i in range(len(A)) ]
        right = [ 0 for i in range(len(A)) ]
        for i in range(1, len(A)):
            left[i] = max(left[i-1], A[i-1])

        for i in range(len(A)-2, 0, -1):
            right[i] = max(right[i+1], A[i+1])

        count = 0
        for i in range(1, len(A)-1):
            count += max(min(left[i], right[i]) - A[i], 0)

        # print left
        # print right

        return count


if __name__ == "__main__":
    print Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])
    print Solution().trap([2,0,2])