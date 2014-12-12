class Solution:
    # @return an integer
    def maxArea(self, height):
        i , j = 0, len(height) -1
        max_volume = 0
        while i < j:
            max_volume = max([max_volume, (j-i) * min([height[i], height[j]]) ])
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_volume


if __name__ == "__main__":
    print Solution().maxArea([1,1])
