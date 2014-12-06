class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0:
            return False

        l = self.searchList(matrix, 0, len(matrix), target)


        return self.searchElement(l, 0, len(l), target)


    def searchList(self, matrix, start_i, end_i, target):
        if start_i == end_i-1:
            return matrix[start_i]

        middle_i = ((start_i + end_i) / 2)

        if matrix[middle_i-1][0] <= target and target < matrix[middle_i][0]:
            return matrix[middle_i-1]
        elif matrix[middle_i][0] > target:
            return self.searchList(matrix, start_i, middle_i, target)
        elif matrix[middle_i][0] <= target:
            return self.searchList(matrix, middle_i, end_i, target)

    def searchElement(self, l, start_i, end_i, target):
        if start_i == end_i-1:
            return l[start_i] == target

        middle_i = ((start_i+ end_i) / 2)

        if target < l[middle_i]:
            return self.searchElement(l, start_i, middle_i, target)
        elif l[middle_i] < target:
            return self.searchElement(l, middle_i, end_i, target)
        else:
            return True

if __name__ == "__main__":
    M = [
            [1,   3,  5,  7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
    ]
    print Solution().searchMatrix(M, 3)

    M = [[1]]

    print Solution().searchMatrix(M, 1)

    M = [[1],[3]]
    print Solution().searchMatrix(M, 3)
