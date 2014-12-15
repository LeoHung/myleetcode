class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        A_l = len(A)

        if A_l <= 1:
            return A_l

        cur = 0
        next = 1
        while next < A_l:
            if A[cur] == A[next]:
                next += 1
            else:
                cur += 1
                A[cur] = A[next]
                next += 1

        return cur + 1

if __name__ == "__main__":
    print Solution().removeDuplicates([1, 1, 2])
    print Solution().removeDuplicates([1])
    print Solution().removeDuplicates([2, 2])
