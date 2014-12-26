class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        A.append(0)
        A_l = len(A)
        i = 0
        while i < len(A) -1:
            if A[i] == i or A[i] is None or A[i] < 0 or A[i] >= A_l:
                i += 1 
                continue
            else:
                if A[i] != A[A[i]]:
                    ind = A[i]
                    A[i] = A[ind]
                    A[ind] = ind
                else:
                    i +=1 
                    continue

        for i in xrange(1, len(A)):
            if A[i] != i:
                return i

        return len(A)

if __name__ == "__main__":
    print Solution().firstMissingPositive([1,2,0])
    print Solution().firstMissingPositive([3,4,-1,1])
    print Solution().firstMissingPositive([2])
            