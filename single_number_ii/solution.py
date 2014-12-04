class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        bit_counts = [ 0 for i in range(32)]
        for a in A:
            for bit_i in range(32):
                if (a & 1 << bit_i) > 0:
                    bit_counts[bit_i] += 1


        ret_int = 0
        for bit_i in range(32):
            if bit_counts[bit_i] % 3 == 1 :
                ret_int |= 1 << bit_i

        if bit_counts[bit_i] %3 == 1:
            ret_int |= ( (~0) << 32)


        return ret_int

if __name__ == "__main__":
    s = Solution()
    print s.singleNumber([1,1,1,3,3,3,9])
    print s.singleNumber([1,1,1,3,3,3,-1])


