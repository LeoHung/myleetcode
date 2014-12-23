class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def fullJustify(self, words, L):
        tmp = []
        count = 0
        ret = []
        for i in range(len(words)):
            w = words[i]
            count += len(w) + 1
            tmp.append(w)
            if i == len(words) - 1:
                l = " ".join(tmp)
                if len(l) < L:
                    l += "".join([" "]* (L - len(l)))
                ret.append(l)
            elif count + len(words[i+1]) > L:
                word_len_sum = 0
                for e in tmp :
                    word_len_sum += len(e)

                last_space = L - word_len_sum 
                if len(tmp) == 1:
                    spaces = [L - word_len_sum]
                else:
                    spaces = [last_space / (len(tmp)-1) ] * (len(tmp)-1)
                    for i in range(last_space % (len(tmp)-1) ):
                        spaces[i] += 1 

                l = ""
                for i in range(len(tmp)-1):
                    l = l + tmp[i] + "".join([" "] * spaces[i])
                
                if len(tmp) == 1 :
                    l = tmp[0] + "".join([" "] * spaces[0])
                else:
                    l = l + tmp[-1]

                ret.append(l)
                tmp = []
                count = 0 
        return ret 

if __name__ == "__main__":
    print Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
