class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        l = len(num)
        tmp = {}
        for e in num:
            if e not in tmp:
                tmp[e] = 0
            
            tmp[e] += 1     
                
            if tmp[e] >= (l+1)/2:
                return e 