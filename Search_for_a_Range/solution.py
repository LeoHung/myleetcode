class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        A_l = len(A)

        start, end = 0, len(A)
        hit_i = None
        # binary search
        while( start < A_l and  not(start == end and A[start] != target) ):
            mid = (start + end)/ 2
            if A[mid] == target:
                hit_i = mid
                break
            elif A[mid] < target:
                start = mid +1
                continue
            else:
                end = mid
                continue

        if hit_i is None:
            return [-1, -1]

        # linear search
        start_i = hit_i
        end_i = hit_i
        while start_i >0 and A[start_i-1] == A[start_i]:
            start_i -= 1


        while end_i > 0 and end_i < A_l-1 and A[end_i+1] == A[end_i]:
            end_i += 1

        return [start_i, end_i]

if __name__ == "__main__":
    print Solution().searchRange([5, 7, 7, 8, 8, 10], 8)
    print Solution().searchRange([2, 2], 3)
