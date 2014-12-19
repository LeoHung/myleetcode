class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if n < 0 :
            sign = -1
            n = -n
        else:
            sign = 1

        shift_base = x 
        ret = 1.0

        for i in range(32):
            if n & (1 << i) > 0:
                ret *= shift_base

            shift_base = shift_base * shift_base 

        if sign < 0:
            ret = 1.0 / ret 
        return ret 

if __name__ == "__main__":
    print Solution().pow(2.0, 2)
    print Solution().pow(2.0, -2)