class Solution:
    # @param num, a list of integer
    # @return an integer
    def maximumGap(self, num):
        n_l = len(num)

        if n_l < 2 :
            return 0
        elif n_l == 2 :
            return abs(num[0]- num[1])

        min_v = min(num)
        max_v = max(num)

        if (1 + max_v - min_v) % (n_l +1) == 0:
            w = (1 + max_v - min_v) / (n_l +1)
        else:
            w = ((1 + max_v - min_v) / (n_l +1)) + 1

        tmp_array = [ [None, None] for i in range(n_l +1) ]

        for n in num:
            ind = (n - min_v) / w 
            # print n, min_v, w, ind
            if tmp_array[ind][0] is None:
                tmp_array[ind][0] = n 
                tmp_array[ind][1] = n
            else:
                tmp_array[ind][0] = min(tmp_array[ind][0], n)
                tmp_array[ind][1] = max(tmp_array[ind][1], n)

        max_gap = 0
        last_max = tmp_array[0][1]
        for tmp in tmp_array[1:]:
            cur_min, cur_max = tmp[0], tmp[1]
            if cur_min is not None:
                max_gap = max(max_gap, cur_min - last_max)
                last_max = cur_max

        return max_gap

if __name__ == "__main__":
    print Solution().maximumGap([1, 2, 3])
    print Solution().maximumGap([0, 0, 0])
    print Solution().maximumGap([2, 1000, 3])