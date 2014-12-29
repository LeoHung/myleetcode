class Solution:
    # @param s, a string
    # @return a boolean

    def isConNumber(self, s):
        if len(s) == 0:
            return False
        nums = [str(i) for i in range(10)]
        for i in range(len(s)):
            if s[i] not in nums:
                return False
        return True

    def isValidLeft(self, s):
        if len(s) == 0:
            return False

        if s[0] == "+" or s[0] == "-":
            s = s[1:]

        for i in range(len(s)):
            if s[i] == ".":
                if len(s[:i]) == 0 and len(s[i+1:]) == 0:
                    return False
                else:
                    return ( (len(s[:i]) == 0) or self.isConNumber(s[:i])) and ( (len(s[i+1:]) == 0) or self.isConNumber(s[i+1:]))

        return self.isConNumber(s)

    def isValidRight(self, s):
        if len(s) == 0:
            return False

        if s[0] == "+" or s[0] == "-":
            s= s[1:]

        return self.isConNumber(s)

    def isNumber(self, s):
        s = s.strip()

        for i in range(len(s)):
            if s[i] == "e":
                return self.isValidLeft(s[:i]) and self.isValidRight(s[i+1:])

        return self.isValidLeft(s)

if __name__ == "__main__":
    print Solution().isNumber("0")
    print Solution().isNumber(" 0.1 ")
    print Solution().isNumber("abc")
    print Solution().isNumber("1 a")
    print Solution().isNumber("2e10")
    print Solution().isNumber("e")
    print Solution().isNumber("e9")
    print Solution().isNumber(".1")
    print Solution().isNumber("-1.")
    print Solution().isNumber("+.8")
    print Solution().isNumber("46.e3")
    print Solution().isNumber("0.e")
    print Solution().isNumber("e.1")
    print Solution().isNumber(".")
    print Solution().isNumber("..")
    print Solution().isNumber("0..")