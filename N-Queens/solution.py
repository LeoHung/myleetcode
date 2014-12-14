class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        self._boards = []
        prev = []
        self.dfs(prev, 0, n)
        return self._boards

    def draw_board(self, q_list, n):
        board = []
        for j in q_list:
            l = [ "." for k in xrange(n) ]
            l[j] = 'Q'
            board.append("".join(l))
        return board

    def dfs(self, prev, i, n):
        if i == n:
            self._boards.append( self.draw_board(prev,n ))

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
    print Solution().solveNQueens(4)
