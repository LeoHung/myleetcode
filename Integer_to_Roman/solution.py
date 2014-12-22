class Solution:
    # @return a string
    def intToRoman(self, num):
        ret = ""
        n1 = num % 10
        n2 = (num % 100) / 10
        n3 = (num % 1000) / 100
        n4 = num / 1000

        n1_num = ["", "I", "II","III", "IV", "V", "VI", "VII", "VIII", "IX"]
        n2_num = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        n3_num = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        n4_num = ["", "M", "MM", "MMM"]

        if n1 != 0:
            ret = n1_num[n1] + ret 
        if n2 != 0:
            ret = n2_num[n2] + ret 
        if n3 != 0:
            ret = n3_num[n3] + ret
        if n4 != 0:
            ret = n4_num[n4] + ret 
        return ret 

if __name__ == "__main__":
    print Solution().intToRoman(4)
    print Solution().intToRoman(44)
    print Solution().intToRoman(444)
    print Solution().intToRoman(9)
    print Solution().intToRoman(99)
    print Solution().intToRoman(999)
    print Solution().intToRoman(60)
    print Solution().intToRoman(1000)