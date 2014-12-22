class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        k = m + n - 1
        i, j = m - 1, n - 1
        while i >= 0 and j >= 0: 
            if A[i] > B[j]:
                A[k] = A[i]
                i -= 1 
                k -= 1 
            else:
                A[k] = B[j]
                j -= 1 
                k -= 1

        while j >= 0:
            A[k] = B[j]
            j -= 1 
            k -= 1

if __name__ == "__main__":
    A = [1, 2, 3 ]
    m = 3
    B = [4, 5, 6 ]
    n = 3
    A.extend(B)
    Solution().merge(A, m, B, n)
    print A