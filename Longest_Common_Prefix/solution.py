class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        n = len(strs)
        if n == 0:
            return ""
        m = min([ len(str) for str in strs] )
        c_p = ""
        for i in range(m):
            c = strs[0][i]
            for n_i in range(1,n):
                if not strs[n_i][i] == c:
                    return c_p

            c_p = c_p + c

        return c_p
