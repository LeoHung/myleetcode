class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        ret = []
        self.genDFS(0, n, 0, ret, [])
        return ret 

    def genDFS(self, i, n, last_parentness, ret, cache):

        if last_parentness > 2*n-i:
            return

        if i == 2 * n and last_parentness == 0:
            ret.append( "".join(cache))
            return 

        if len(cache) == 0:
            cache.append("(")
            self.genDFS(i+1, n, last_parentness+1, ret, cache)
            cache.pop()
        else: 
            if last_parentness > 0:
                cache.append(")")
                self.genDFS(i+1, n, last_parentness-1, ret, cache)
                cache.pop()

            cache.append("(")
            self.genDFS(i+1, n, last_parentness+1, ret, cache)
            cache.pop()

if __name__ == "__main__":
    print Solution().generateParenthesis(3)

