class Solution:
    # @return an integer
    def romanToInt(self, s):

        n1_num = ["", "I", "II","III", "IV", "V", "VI", "VII", "VIII", "IX"]
        n2_num = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        n3_num = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        n4_num = ["", "M", "MM", "MMM"]

        ret = 0
        i = 0 
        for k in range(len(n4_num)-1, 0, -1):
            e = n4_num[k]
            if s[i:].startswith(e): 
                ret += k * 1000
                i += len(e)

        for k in range(len(n3_num)-1, 0, -1):
            e = n3_num[k]
            if s[i:].startswith(e): 
                ret += k * 100
                i += len(e)

        for k in range(len(n2_num)-1, 0, -1):
            e = n2_num[k]
            if s[i:].startswith(e): 
                ret += k * 10
                i += len(e)

        for k in range(len(n1_num)-1, 0, -1):
            e = n1_num[k]
            if s[i:].startswith(e): 
                ret += k 
                i += len(e)

        return ret 

if __name__ == "__main__":
    s = Solution()
    print s.romanToInt("MCMLIV") 
    print s.romanToInt("MCMLIV") == 1954
    print s.romanToInt("MCMXC")
    print s.romanToInt("MCMXC") == 1990
    print s.romanToInt("MMXIV")
    print s.romanToInt("MMXIV") == 2014

