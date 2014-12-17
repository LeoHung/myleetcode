class Solution:
    # @return a boolean
    def isValid(self, s):
        last = list()
        for i in range(len(s)):
            e = s[i]
            if e in ["}", ")", "]"]:
                if len(last) == 0:
                    return False
                if e == "}" and last[-1] != "{":
                    return False
                if e == ")" and last[-1] != "(":
                    return False
                if e == "]" and last[-1] != "[":
                    return False
                last.pop()
            else:
                last.append(e)
        return len(last) == 0

if __name__ == "__main__":
    print Solution().isValid("()[]{}")
    print Solution().isValid("()")
    print Solution().isValid("(]")
    print Solution().isValid("([)]")