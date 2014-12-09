class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        D = {}
        for w1_i in range(len(word1)+1):
            for w2_i in range(len(word2)+1):
                if w1_i == 0:
                    D[(w1_i, w2_i)] = w2_i
                    continue
                if w2_i == 0:
                    D[(w1_i, w2_i)] = w1_i
                    continue

                c1 = word1[w1_i - 1]
                c2 = word2[w2_i - 1]
                if c1 == c2:
                    D[(w1_i, w2_i)] = D[(w1_i-1, w2_i-1)]
                else:
                    D[(w1_i, w2_i)] = min([
                                            D[(w1_i-1, w2_i-1)] +1,
                                            D[(w1_i, w2_i-1)] +1,
                                            D[(w1_i-1, w2_i)] +1
                                        ])
        return D[(w1_i, w2_i)]

if __name__ == "__main__":

    print Solution().minDistance("no", "nil")
