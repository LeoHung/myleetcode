class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def copyList(self, l):
        return [v for v in l]
    
    def list2str(self, l):
        return ".".join( [ str(v) for v in l]) 
    def subsetsWithDup(self, S):
        S = sorted(S)
        visited = set()

        ret = []
        S_l = len(S)
        for round in range(2 ** S_l):
            one_set = []
            for r_i in range(S_l):
                if (1 << r_i & round) > 0:
                    one_set.append(S[r_i])
            
            one_set_str = self.list2str(one_set)
            if not one_set_str in visited:
                ret.append(one_set)
                visited.add(one_set_str)
                
        return ret 
