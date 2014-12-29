class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        # s += "\t"
        # p += "\t"
        s_l = len(s)
        p_l = len(p)

        s_i = 0
        p_i = 0
        isStar = False

        s_tmp = 0
        p_tmp = 0

        while s_i < s_l:
            if p_i < p_l and (s[s_i] == p[p_i] or p[p_i] == '?'):
                s_i += 1 
                p_i += 1
            elif p_i < p_l and p[p_i] == '*':
                isStar = True
                s_tmp = s_i
                while p_i < p_l and p[p_i] == '*':
                    p_i +=1 
                p_tmp = p_i
            elif isStar and (p_i == p_l or (p_i < p_l and p[p_i] != s[s_i])):
                s_tmp += 1 
                s_i = s_tmp
                p_i = p_tmp
            else:
                return False

        while p_i < p_l and p[p_i] == '*':
            p_i += 1

        return (p_i == p_l)

if __name__ == "__main__":
    print Solution().isMatch("abc", "a*bc")
    print Solution().isMatch("abc", "a*b*c")
    print Solution().isMatch("abc", "a*b**c")
    print Solution().isMatch("absfsdfsfc", "a*b**c")
    print Solution().isMatch("absfsdfsfc", "a*bc")
    print Solution().isMatch("aa", "a")
    print Solution().isMatch("abc", "*")
    print Solution().isMatch("hi", "*?")
    print Solution().isMatch("babaaabbaaaaaaaabbbbaabaababbbaababbaaaaabaabbbbaaaaba", "****a**b**b***ba*ab*")
    print Solution().isMatch("asaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "")