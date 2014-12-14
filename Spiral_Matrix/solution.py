class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        N = len(matrix)
        if N == 0:
            return []
        M = len(matrix[0])

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ret = []

        direction_i = 0
        direction = directions[direction_i]
        expect_size = N*M
        x, y = 0, 0

        while len(ret) < expect_size:
            if x < 0 or x > N - 1 or y < 0 or y > M - 1 or matrix[x][y] is None:

                x, y = x - direction[0], y - direction[1]
                direction_i = (direction_i + 1) % 4
                direction = directions[direction_i]
                x, y = x + direction[0], y + direction[1]
                continue

            ret.append(matrix[x][y])
            matrix[x][y] = None

            x, y = x + direction[0], y + direction[1]

        return ret

if __name__ == "__main__":
    print Solution().spiralOrder(
    [
        [ 1, 2, 3 ],
        [ 4, 5, 6 ],
        [ 7, 8, 9 ]
    ]
    )

    print Solution().spiralOrder(
    [
        [ 2,3 ]

    ]
    )

