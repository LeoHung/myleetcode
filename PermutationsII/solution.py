class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers


    def permuteUnique(self, num):
        sorted_num = sorted(num)
        self.num_length = len(sorted_num)

        visited = [ False for i in range(len(sorted_num)) ]

        self.ans = []

        sample = []

        self.dfs(sorted_num, visited, sample, 0)

        return self.ans

    def dfs(self, num, visited, sample, num_of_visited):
        if(num_of_visited == self.num_length):
            copySample = [x  for x in sample]
            self.ans.append(copySample)
            return

        for i in xrange(self.num_length):
            if visited[i]:
                continue
            elif not visited[i] and (i == 0 or ( i >0 and (not num[i] == num[i-1]) or (num[i] == num[i-1] and visited[i-1] == True))) :
                sample.append(num[i])
                visited[i] = True
                self.dfs(num, visited, sample, num_of_visited+1)
                del(sample[-1])
                visited[i] = False
        return


if __name__ == "__main__":

    s = Solution()
    print s.permuteUnique([2, 2, 1, 1])

