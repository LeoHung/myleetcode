class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows == 0 :
            return []
            
        ret = []
        for i in xrange(numRows):
            if i == 0:
                ret.append([1])
                continue
            row = []
            for j in xrange(i+1):
                if j == 0:
                    row.append(1)
                elif j == i:
                    row.append(1)
                else:
                    row.append(ret[i-1][j-1] + ret[i-1][j])
            ret.append(row)
        return ret
if __name__ == "__main__":
    s = Solution()
    for i in range(10):
        print s.generate(i)
