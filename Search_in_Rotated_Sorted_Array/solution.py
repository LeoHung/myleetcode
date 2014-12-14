class Solution:

    def searchBoundary(self, A, start, end):
        mid = (start + end) /2

        if (end - start) <= 3:
            if A[start] > A[mid] :
                return start
            elif A[mid] > A[end-1]:
                return mid
            return end -1

        if A[start] > A[mid]:
            return self.searchBoundary(A, start, mid+1)
        else:
            return self.searchBoundary(A, mid, end)

    def bs(self, A, start, end, target):

        while(start < len(A) and not(start == ((start+end)/2) and A[start] != target)):

            mid = (start + end)/2


            if A[mid] == target:
                return mid

            if A[mid] < target:
                start = mid + 1
            else:
                end = mid

        return None

    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        if A[0] < A[-1]:
            b = len(A) -1

        else:
            b = self.searchBoundary(A, 0, len(A))

        i = self.bs(A, 0, b+1, target)
        if i is not None:
            return i

        i = self.bs(A, b+1, len(A), target)
        if i is not None:
            return i
        else:
            return -1


if __name__ == "__main__":
    print Solution().search([4, 5, 6, 7, 0, 1, 2], 4)
    print Solution().search([4, 5, 6, 7, 0, 1, 2], 5)
    print Solution().search([4, 5, 6, 7, 0, 1, 2], 6)
    print Solution().search([4, 5, 6, 7, 0, 1, 2], 7)
    print Solution().search([4, 5, 6, 7, 0, 1, 2], 0)
    print Solution().search([4, 5, 6, 7, 0, 1, 2], 1)
    print Solution().search([4, 5, 6, 7, 0, 1, 2], 2)
    print Solution().search([1], 0)
    print Solution().search([3, 1], 2)
    print Solution().search([3,5,1], 5)
