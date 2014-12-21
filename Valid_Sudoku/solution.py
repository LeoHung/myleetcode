class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        for i in range(9):
            tmp = [False for k in range(10) ]
            for j in range(9):
                v = board[i][j]
                if v == ".":
                    continue
                else:
                    v = int(board[i][j])
                    if tmp[v] == True:
                        return False
                    else:
                        tmp[v] = True

        for j in range(9):
            tmp = [False for k in range(10) ]
            for i in range(9):
                v = board[i][j]
                if v == ".":
                    continue
                else:
                    v = int(board[i][j])
                    if tmp[v] == True:
                        return False
                    else:
                        tmp[v] = True

        start_is = range(0, 9, 3)
        start_js = range(0, 9, 3)

        for start_i in start_is:
            for start_j in start_js:
                tmp = [False for k in range(10) ] 
                for d_i in range(3):
                    for d_j in range(3):
                        i = start_i + d_i
                        j = start_j + d_j

                        v = board[i][j]
                        if v == ".":
                            continue
                        else:
                            v = int(board[i][j])
                            if tmp[v] == True:
                                return False
                            else:
                                tmp[v] = True
        return True
