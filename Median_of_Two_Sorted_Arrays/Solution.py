class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        m = len(A)
        n = len(B)
        if( (m + n) % 2 == 0):
            k = (m+n)/2 
            return (float(self.find_k( A, m , B, n, k)) + float(self.find_k(A, m, B, n, k+1))) /2.0 
        else:
            k = (m+n)/2 + 1
            return self.find_k(A, m, B, n, k)
    
    def find_k(self, A, m, B, n , k):
        #print A, m, B, n, k
        if m > n :
            return self.find_k( B, n, A, m, k)
        
        if m == 0:
            return B[k-1]

        pa = min([m, k/2])
        pb = k - pa

        if k == 1:
            return min([A[0], B[0]])

        if(A[pa-1] == B[pb-1]):
            return A[pa-1]
        elif A[pa-1] > B[pb-1]:
            if pb < len(B):
                return self.find_k(A, m, B[pb:], n -(pb), k-pb )
            else:
                return self.find_k(A, m, [], 0, k-pb)
        else:
            if pa < len(A):
                return self.find_k([], 0, B, n, k-pa)
            else:
                return self.find_k(A[pa:], m-(pa), B, n, k-pa)
        
if __name__ == "__main__":
    s = Solution()
    print s.findMedianSortedArrays( [1,2, 3], [ 5, 6, 8])
    print s.findMedianSortedArrays([],[1])
    print s.findMedianSortedArrays([1],[1])

        
