class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        A_l = len(A)

        if A_l <= 2:
            return A_l

        cur, next = 0, 1
        last_count = 0
        while next < A_l:
            if A[next] == A[next - 1]:
                last_count += 1
            else:
                last_count = 0

            if last_count < 2:
                cur += 1
                A[cur] = A[next]

            next += 1

        return cur +1

if __name__ == "__main__":
    print Solution().removeDuplicates([1,1,1,2,2,3])
