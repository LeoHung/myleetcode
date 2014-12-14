class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        ret = []
        cache = []
        cache_sum = 0
        candidates = sorted(candidates)
        self.dfs(candidates, 0, target, cache, cache_sum, ret)
        return ret

    def dfs(self, candidates, i, target, cache, cache_sum, ret):
        if i >= len(candidates) :
            return
        if cache_sum > target:
            return
        if cache_sum == target:
            if not cache in ret:
                ret.append([e for e in cache])

        for j in range(i, len(candidates)):
            cache.append(candidates[j])
            cache_sum += candidates[j]

            self.dfs(candidates, j, target, cache, cache_sum, ret )

            cache_sum -= candidates[j]
            cache.pop()

if __name__ == "__main__":
    print Solution().combinationSum([2,3,6,7], 7)
