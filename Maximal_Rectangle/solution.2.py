class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):

        max_area = 0 
        N = len(matrix)
        if N == 0:
            return 0
        M = len(matrix[0])
        height = [0] * (M+1)
        for i in range(N):
            for j in range(M):
                if matrix[i][j] == "1":
                    height[j] = height[j] + 1
                else:
                    height[j] = 0

            s = list()
            s_l = 0 
            for j in range(M+1):
                if s_l == 0 or height[s[-1]] <= height[j]:
                    s.append(j)
                    s_l += 1 
                else:
                    while s_l > 0 and height[s[-1]] > height[j]:
                        ind = s.pop()
                        s_l -= 1
                        if len(s) == 0:
                            w = j  
                        elif len(s) > 0:
                            w = j - s[-1] -1
                        max_area = max(max_area, w * height[ind])

                    s.append(j)
                    s_l += 1 
        return max_area           



if __name__ == "__main__":
    m = ["01101","11010","01110","11110","11111","00000"]
    print Solution().maximalRectangle(m)