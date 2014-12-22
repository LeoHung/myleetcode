class Solution:
    # @return a string
    def minWindow(self, S, T):
        if len(T) > len(S):
            return ""

        T_l = len(T)

        dic = {}
        for s in T:
            if s not in dic:
                dic[s] = 0
            dic[s] += 1 

        minLen = len(S)
        minStr = ""

        left, right = 0, 0
        count = 0 

        for right in range(len(S)):
            if S[right] in dic:
                if dic[S[right]] > 0:
                    count += 1 
                dic[S[right]] -= 1
            
            while count == len(T):
                if minLen >= (right - left + 1):
                    minLen = right - left + 1 
                    minStr = S[left:right+1]
                
                if S[left] in dic:
                    dic[S[left]] += 1
                    if dic[S[left]] > 0:
                        count -= 1
                left += 1 

        return minStr

if __name__ == "__main__":
    print Solution().minWindow("ADOBECODEBANC", "ABC")
    print Solution().minWindow("A", "A")