class Solution:
    # @return an integer
    def totalNQueens(self, n):
        self.count = 0
        prev = []
        self.dfs(prev, 0, n)
        return self.count

    def dfs(self, prev, i, n):
        if i == n:
            self.count += 1

        for j in range(n):
            if j in prev:
                continue

            notValid = False

            for prev_i, prev_j in enumerate(prev):
                if abs(prev_i - i) == abs(prev_j - j):
                    notValid = True
                    break
            if notValid:
                continue

            prev.append(j)
            self.dfs(prev, i+1, n)
            prev.pop()

if __name__ == "__main__":
    print Solution().totalNQueens(4)
