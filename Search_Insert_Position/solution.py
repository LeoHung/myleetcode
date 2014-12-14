class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        return self.bs(0, len(A), A, target)

    def bs(self, start, end, A, target):
        mid = (start + end) / 2
        if start == end or A[mid] == target:
            return mid
        elif A[mid] < target:
            return self.bs(mid+1, end, A, target)
        else:
            return self.bs(start, mid, A, target)

if __name__ == "__main__":
    print Solution().searchInsert([1,3,5,6], 5)
    print Solution().searchInsert([1,3,5,6], 2)
    print Solution().searchInsert([1,3,5,6], 7)
    print Solution().searchInsert([1,3,5,6], 0)
