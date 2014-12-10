class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.

    def setPreZero(self, matrix, n_i, m_i, N, M):
        for m_j in xrange(M):
            if not matrix[n_i][m_j] == 0:
                matrix[n_i][m_j] = None

        for n_j in xrange(N):
            if not matrix[n_j][m_i] == 0:
                matrix[n_j][m_i] = None

    def setZeroes(self, matrix):
        N = len(matrix)
        if N <= 0:
            return
        M = len(matrix[0])
        if M <= 0:
            return

        for n_i in xrange(N):
            for m_i in xrange(M):
                if matrix[n_i][m_i] == 0:
                    self.setPreZero(matrix, n_i, m_i, N, M)

        # clear None to zero

        for n_i in xrange(N):
            for m_i in xrange(M):
                if matrix[n_i][m_i] == None:
                    matrix[n_i][m_i] = 0

