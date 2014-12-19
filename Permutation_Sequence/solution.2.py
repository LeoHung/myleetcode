class Solution:
    # @return a string
    def factorial(self, n):
        if n == 0:
            return 1

        ret = 1
        for i in range(2,n+1):
            ret *= i 
        return ret

    def getPermutation(self, n, k):
        k -= 1 
        ret = ""

        num_str = [str(i) for i in range(1, n+1)]
        for i in range(n-1, -1, -1):
            fac = self.factorial(i)
            ind = (k /fac)
            ret += num_str[ind]
            del num_str[ind]

            k = k % fac
        return ret 

if __name__ == "__main__":
    print Solution().getPermutation(3, 1)
    print Solution().getPermutation(3, 2)
    print Solution().getPermutation(3, 3)
    print Solution().getPermutation(3, 4)
    print Solution().getPermutation(3, 5)
    print Solution().getPermutation(3, 6)

    print Solution().getPermutation(8, 37565)

