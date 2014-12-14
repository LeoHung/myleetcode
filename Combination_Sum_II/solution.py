class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        ret = []
        cache = []
        cache_sum = 0
        candidates = sorted(candidates)
        c_l = len(candidates)
        self.dfs(candidates, c_l, 0, target, cache, cache_sum, ret)
        return ret

    def dfs(self, candidates, c_l, i, target, cache, cache_sum, ret):

        if cache_sum == target:
            # if not cache in ret:
            ret.append(list(cache))
            return

        if i >= c_l:
            return

        for j in range(i, c_l):
            if candidates[j] + cache_sum <= target and (i == j or candidates[j] != candidates[j-1]):

                cache.append(candidates[j])
                cache_sum += candidates[j]

                self.dfs(candidates, c_l, j+1, target, cache, cache_sum, ret )

                cache_sum -= candidates[j]
                cache.pop()

if __name__ == "__main__":
    print Solution().combinationSum2([10,1,2,7,6,1,5], 8)
    print Solution().combinationSum2([1], 1)
