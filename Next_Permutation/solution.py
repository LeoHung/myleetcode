class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        max_v = num[-1]
        max_i = len(num) -1
        start_i = None
        for i in range(len(num)-1, 0 - 1, -1):
            if num[i] < max_v:
                start_i = i
                break
            else:
                max_v = num[i]
                max_i = i



        if start_i is not None:
            to_change_i = None
            to_change_v = None
            for j in range(start_i+1, len(num)):
                if num[j] > num[start_i] and (to_change_v == None or num[j] < to_change_v):
                    to_change_i = j
                    to_change_v = num[j]

            num[start_i], num[to_change_i] = num[to_change_i], num[start_i]
            num[start_i+1:] = sorted(num[start_i+1:])
        else:
            num = sorted(num)

        return num

if __name__ == "__main__":
    print Solution().nextPermutation([1,2,3])
    print Solution().nextPermutation([3,2,1])
    print Solution().nextPermutation([1,1,5])
    print Solution().nextPermutation([2,3,1])
    print Solution().nextPermutation([1,3,2])