class Solution:
    def isValid(self, board):
        for i in range(9):
            tmp = set()
            for j in range(9):
                if board[(i,j)] is None:
                    continue 
                if board[(i,j)] in tmp:
                    return False

                tmp.add(board[(i,j)])
        
        for j in range(9):
            tmp = set()
            for i in range(9):
                if board[(i,j)] is None:
                    continue 
                if board[(i,j)] in tmp:
                    return False
                tmp.add(board[(i,j)])

        for i_start in range(0, 9, 3):
            for j_start in range(0, 9, 3):
                tmp = set()
                for d_i in range(3):
                    for d_j in range(3):
                        i = i_start + d_i
                        j = j_start + d_j
                        if board[(i,j)] is None:
                            continue
                        if board[(i,j)] in tmp:
                            return False
                        tmp.add(board[(i,j)])
        return True


    def genDictBoard(self, board):
        dict_board = {}
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    dict_board[(i,j)] = None
                else:
                    dict_board[(i,j)] = int(board[i][j])
        return dict_board

    def genEmptySlots(self, dict_board):
        ret = list()
        for i in range(9):
            for j in range(9):
                if dict_board[(i,j)] is None:
                    ret.append((i,j))
        return ret 
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        dict_board = self.genDictBoard(board)
        empty_slots = self.genEmptySlots(dict_board)

        dict_board = self.dfs(dict_board, empty_slots)

        for i in range(9):
            tmp_line = ""
            for j in range(9):
                tmp_line += str(dict_board[(i,j)])
            board[i] = tmp_line

    def genCandidates(self, dict_board, p_i, p_j):
        ret = range(1, 10)

        for i in range(9):
            if dict_board[(i, p_j)] is not None:
                try:
                    ret.remove(dict_board[(i, p_j)])
                except:
                    pass

        for j in range(9):
            if dict_board[(p_i, j)] is not None:
                try:
                    ret.remove(dict_board[(p_i, j)])
                except:
                    pass

        i_start = (p_i / 3) * 3 
        j_start = (p_j / 3) * 3
        for d_i in range(3):
            for d_j in range(3):
                i = i_start + d_i
                j = j_start + d_j
                if dict_board[(i,j)] is not None:
                    try:
                        ret.remove(dict_board[(i,j)])
                    except:
                        pass
        return ret 

    def dfs(self, dict_board, empty_slots):
        # self.print_board(dict_board)

        if len(empty_slots) == 0:
            return dict_board

        # find first slot:
        p_i, p_j = empty_slots.pop()

        candidates = self.genCandidates(dict_board, p_i, p_j)
        for c in candidates:
            dict_board[(p_i, p_j)] = c
            tmp = self.dfs(dict_board, empty_slots)
            if tmp is not None:
                return dict_board
            dict_board[(p_i, p_j)] = None


        empty_slots.append((p_i, p_j))
        return None

    def print_board(self, dict_board):
        for i in range(9):
            l = ""
            for j in range(9):
                if dict_board.get((i,j)) is None:
                    l += "."
                else:
                    l += str(dict_board[(i,j)])
            print l 

if __name__ == "__main__":
    board = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
    Solution().solveSudoku(board)
    print board