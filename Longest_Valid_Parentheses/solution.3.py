class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        stack = list()
        max_v = 0 
        tmp = []
        for i, e in enumerate(s):
            if e == '(':
                tmp.append(e)
            elif e == ')':        
                if len(tmp) > 0:
                    if tmp[-1] == '(':
                        tmp.pop()
                        count = 2
                        while len(tmp) > 0 and type(tmp[-1]) == int:
                            count += tmp.pop()

                        tmp.append(count)

                    elif type(tmp[-1]) == int and len(tmp) >= 2 and tmp[-2] == '(':
                        count = 2 
                        count += tmp.pop()
                        tmp.pop()
                        while len(tmp) > 0 and type(tmp[-1]) == int:
                            count += tmp.pop()

                        tmp.append(count)
                    else:
                        tmp.append(e)

        for e in tmp:
            if type(e) == int:
                max_v = max(max_v, e)

        return max_v
        
if __name__ == "__main__":
    print Solution().longestValidParentheses("(()")
    print Solution().longestValidParentheses(")()())")
    print Solution().longestValidParentheses("()()")
    print Solution().longestValidParentheses("()(()")
    print Solution().longestValidParentheses("()(())")
    print Solution().longestValidParentheses("(()())")
    print Solution().longestValidParentheses(")(((((()())()()))()(()))("
)
    