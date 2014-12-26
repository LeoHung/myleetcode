class Solution:
    # @return a boolean
    def isScramble(self, s1, s2):
        if len(s1) != len(s2):
            return False
        if len(s1) == 1:
            return s1 == s2

        tmp_s1 = sorted(list(s1))
        tmp_s2 = sorted(list(s2))
        if tmp_s1 != tmp_s2:
            return False

        for i in range(1, len(s1)):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            elif self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                return True

        return False

if __name__ == "__main__":
    print Solution().isScramble("a", "a")
    print Solution().isScramble("ab", "ba")
    print Solution().isScramble("rgtae", "great")
    print Solution().isScramble("rgtae", "grrat")
    print Solution().isScramble("b", "a")
    print Solution().isScramble("eswjvddvalysqvfywjvcywpwssqgzt", "vwsyywweljdftwsjqdpzassgcyvvqv") 