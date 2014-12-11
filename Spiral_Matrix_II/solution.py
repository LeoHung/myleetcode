class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        if n == 0:
            return None

        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        M = [ [ None for j in range(n) ] for i in range(n)]

        c = 1
        i, j = 0 , 0
        back_i, back_j = 0, 0

        d_i = 0
        next_dir = direction[d_i]
        while c <= n**2:
            if i < 0 or i >= n or j <0 or j >=n not M[i][j] == None :
                d_i = (d_i +1) % 4
                next_dir = direction[d_i]
                c -= 1
                i, j = back_i, back_j


            M[i][j] = c
            c +=1

            back_i, back_j = i, j
            i, j = i + next_dir[0], j + next_dir[1]

        return M
