class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        height.append(0)
        s = list()

        max_area = 0
        j = 0 
        for i in range(len(height)):
            if len(s) == 0 or height[s[-1]] <= height[i] :
                s.append(i)
            else: 
                while len(s) > 0 and height[s[-1]] > height[i]:
                    ind = s.pop()
                    if len(s) > 0:
                        w = i - s[-1] -1
                    else:
                        w = i 
                    max_area = max(height[ind] * w, max_area, max_area)
                s.append(i)
        return max_area

if __name__ == "__main__":
    print Solution().largestRectangleArea([2,1,2])
    print Solution().largestRectangleArea([2,1,5,6,2,3])