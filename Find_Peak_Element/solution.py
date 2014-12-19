class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        for i in range(1, len(num) -1):
            if num[i-1]  < num[i] and num[i] > num[i+1]:
                return i

        if len(num) == 1:
            return 0

        if len(num) >= 2:
            if num[0] > num[1]:
                return 0
            if num[-1] > num[-2]:
                return len(num) -1 

