class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        if len(S) == 0:
            return []

        ret = []
        S = sorted(S)
        s_len = len(S)


        for round_i in range(2 **  s_len):
            row = []
            for j in range(s_len):
                if 1<<j & round_i > 0:
                    row.append(S[j])
            ret.append([v for v in row])

        return ret

if __name__ == "__main__":
    print Solution().subsets([1,2,3])
