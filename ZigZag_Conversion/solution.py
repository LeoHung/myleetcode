class Solution:
    # @return a string
    def convert(self, s, nRows):
        ret = ""
        s_l = len(s)
        g_l = nRows + nRows - 2

        if nRows < 2:
            return s

        for i in range(nRows):
            if i == 0 or i == nRows - 1:
                for j in range(i, s_l, g_l):
                    ret += s[j]
            else:
                for j in range(i, s_l, g_l):
                    ret += s[j]
                    k = (j -i) + (g_l-i)
                    if k < s_l:
                        ret += s[k]
        return ret 

if __name__ == "__main__":
    print Solution().convert("PAYPALISHIRING", 3)