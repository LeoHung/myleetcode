class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        h_l = len(haystack)
        n_l = len(needle)
        if n_l > h_l:
            return -1
        if n_l == 0:
            return 0


        F = self.genF(needle)
        i, j = 0, 0

        while i < h_l - n_l+1 :
            j = 0 

            while i + j < h_l and j < n_l :
                if haystack[i+j] == needle[j]:
                    j += 1  
                else:
                    if F[j] == 0 :
                        break
                    i = i + (j - F[j])
                    j = F[j]
                    
            if j == n_l:
                return i

            if F[j] == 0:
                i = i+ 1

        return -1 

    def genF(self, needle):
        i, j, k = 0, 0, 0        
        F = [ 0 ] * len(needle)

        i = 1
        while i < len(needle):
            j = 0 
            while i+j < len(needle) and needle[i+j] == needle[j]:
                F[i+j] = j 
                j+=1

            i = i + j + 1

        return F

if __name__ == "__main__":
    print Solution().strStr("shikisfatabababahahaha","abababab")
    print Solution().strStr("bbaabbbaaabaabbbbaababbaabbaababaabbbaaaabaaabaababbbababaaaabbabbabbababbaaaaabbbbabaaabbabaabbbbaabbababbabbaaabbbbbbaaabaababaa", "aaababababbb")
    print Solution().strStr("a", "a")
    # print Solution().genF("aaaaaaaaa")
    # print Solution().genF("abababab")