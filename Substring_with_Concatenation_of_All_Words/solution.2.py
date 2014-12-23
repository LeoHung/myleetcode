class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        s_l = len(S)
        l_l = len(L)
        w_l = len(L[0])
        ret = []

        for k in range(w_l):
            d = {}
        
            for e in L:
                if e not in d:
                    d[e] = 0
                d[e] += 1

            count = 0
            left = k

            for right in xrange(k, s_l, w_l):
                e = S[right:right+w_l]

                if e not in d:
                    while left < right:
                        e2 = S[left:left+w_l]
                        if e2 in d:
                            d[e2] += 1
                            count -= 1                             
                        left += w_l                    
                elif d[e] == 0:
                    while left < right:
                        e2 = S[left:left+w_l]
                        if e2 in d:
                            d[e2] += 1
                            count -= 1 
                            if d[e] > 0: 
                                left += w_l
                                break 
                        left += w_l
                    d[e] -= 1 
                    count += 1 
                elif e in d and d[e] > 0:
                    d[e] -= 1 
                    count += 1 

                if count == l_l:
                    while S[left:left+w_l] not in d and left < right:
                        left += w_l

                    ret.append(left)
                    d[S[left:left+w_l]] += 1
                    count -= 1 
                    left += w_l

        return ret 


if __name__ == "__main__":
    print Solution().findSubstring("barfoothefoobarman", ["foo", "bar"])
    print Solution().findSubstring("abababab", ["a","b","a"])