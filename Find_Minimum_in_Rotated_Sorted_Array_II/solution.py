class Solution:
    def findRange(self, left, right, num): 
        if right - left <= 1:
            return None
        elif right - left == 2:
            if num[left] > num[left+1]:
                return left + 1
            else:
                return None
        elif right - left == 3:
            if num[left] > num[left+1]:
                return left +1 
            elif num[left+1] > num[left+2]:
                return left +2 
            else:
                return None

        mid = (left + right) / 2 
        if  num[left] < num[mid]:
            return self.findRange(mid, right, num)
        elif num[left] > num[mid]:
            return self.findRange(left, mid+1, num)
        else:
            tmp = self.findRange(left, mid+1, num)
            if tmp is not None:
                return tmp
            return self.findRange(mid, right, num)

    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        min_ind = self.findRange(0, len(num), num)
        if min_ind == None:
            if len(num) > 0:
                return num[0]
            else:
                return None
        else:
            return num[min_ind]
if __name__ == "__main__":
    print Solution().findMin([4, 5, 6, 7, 8, 1, 2, 2 , 4])

    print Solution().findMin([1])
