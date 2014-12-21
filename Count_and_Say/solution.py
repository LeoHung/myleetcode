class Solution:
    # @return a string
    def countAndSay(self, n):
        if n == 1:
            return "1"
        last = self.countAndSay(n-1)
        i = len(last) - 1 

        ret = ""

        while i >= 0:
            base = last[i]
            count = 1 
            j = i - 1
            while j >= 0 and last[j] == base:
                count += 1
                j -= 1
            ret = (str(count) + base + ret)
            i = j  
        return ret 


if __name__ == "__main__":
    print Solution().countAndSay(1)
    print Solution().countAndSay(2)
    print Solution().countAndSay(3)
    print Solution().countAndSay(4)
    print Solution().countAndSay(5)
    print Solution().countAndSay(6)
