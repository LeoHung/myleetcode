class Solution:
    # @return a list of lists of integers



    def dp(self, k, n , i, c_list):
        c_list.append(i)

        if len(c_list) == k:
            self.ret.append( [v for v in c_list])
            c_list.pop()
            return

        for j in range(i+1, n+1):
            self.dp(k, n, j, c_list)

        c_list.pop()


    def combine(self, n, k):
        self.ret = []

        c_list = []

        for i in range(1, n+1):
            self.dp(k, n, i, c_list)

        return self.ret

if __name__ == "__main__":

    print Solution().combine(4, 2)
