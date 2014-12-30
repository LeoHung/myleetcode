class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        dp = {}
        for s_i in range(len(s)+1):
            for p_i in range(len(p)+1):
                dp[(s_i, p_i)] = False

        dp[(0, 0)] = True
        
        for p_i in range(2, len(p)+1):
            if p[p_i-1] == '*': 
                dp[(0, p_i)] = dp[(0, p_i-2)]

        for s_i in xrange(1, len(s)+1):
            for p_i in xrange(1, len(p)+1):
                if p[p_i-1] == '*':
                    dp[(s_i, p_i)] = dp[(s_i, p_i-1)] or dp[(s_i, p_i-2)] or (dp[(s_i-1, p_i)] and (s[s_i-1] == p[p_i-2] or p[p_i-2] == "."))
                else:
                    dp[(s_i, p_i)] = dp[(s_i-1, p_i-1)] and (s[s_i-1] == p[p_i-1] or p[p_i-1] == '.')

        return dp[(len(s), len(p))]

if __name__ == "__main__":
    for x, y in [
        # ("aa", "a"), 
        # ("aa", "aa"), 
        # ("aaa", "aa"),
        # ("aa", "a*"), 
        # ("aa", ".*"), 
        ("ab", ".*"), 
        # ("aab", "c*a*b"),
        # ("a", ".*..a*"),
        ("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c")
        ]:
        print Solution().isMatch(x, y)