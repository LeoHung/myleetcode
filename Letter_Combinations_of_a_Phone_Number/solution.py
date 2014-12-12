class Solution:
    # @return a list of strings, [s1, s2]
    def gen(self,output_list, cur_list, d2c, i, digits, d_l ):
        if i == d_l:
            output_list.append("".join(cur_list))
            return

        cur_d = digits[i]
        for c in d2c[cur_d]:
            cur_list.append(c)
            self.gen(output_list, cur_list, d2c, i+1, digits, d_l)
            cur_list.pop()

    def letterCombinations(self, digits):
        d2c = {
                '0':[" "] ,
                '2':["a","b","c"],
                '3':['d','e','f'],
                '4':['g','h','i'],
                '5':['j','k','l'],
                '6':['m','n','o'],
                '7':['p','q','r','s'],
                '8':['t','u','v'],
                '9':['w','x','y','z']
            }

        output_list = []
        cur_list = []
        self.gen(output_list, cur_list, d2c, 0, digits, len(digits))
        return output_list

if __name__ == "__main__":
    print Solution().letterCombinations("22")
