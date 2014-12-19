class Solution:
    def findMedianSortedArrays(self, A, B):
        A_l, B_l = len(A), len(B)
        m_i = (A_l + B_l) / 2 
        if (A_l + B_l) % 2 == 0:
            return float(
                self.findK(A, B, m_i+1) +
                self.findK(A, B, m_i)
            ) / 2.0
        else:
            return float(self.findK(A, B, m_i+1))

    def findK(self, A, B, k):
        # print A, B, k
        A_l, B_l = len(A), len(B)
        if B_l < A_l:
            return self.findK(B, A, k)

        if A_l == 0:
            return B[k-1]

        if k == 1: 
            return min(A[0], B[0])

        pa = min([k/2, A_l])
        pb = k - pa

        # print pa, pb

        if A[pa-1] < B[pb-1]:
            return self.findK(A[pa:], B, k-(pa))
        elif A[pa-1] > B[pb-1]:
            return self.findK(A, B[pb:], k-(pb))
        else:
            return A[pa-1]

if __name__ == "__main__":
    print Solution().findMedianSortedArrays([1,2,3],[4,5,6])
    print Solution().findMedianSortedArrays([4,5,6],[1,2,3])
    print Solution().findMedianSortedArrays([1,2], [1,2])
    print Solution().findMedianSortedArrays([2], [1,3])
    print Solution().findMedianSortedArrays([], [1])
