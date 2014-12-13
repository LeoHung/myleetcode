class Solution:

    def genHash(self, num):
        ret = {}
        num_l = len(num)
        for i in range(num_l):
            for j in range(i+1, num_l):
                half = num[i] +num[j]
                if not half in ret:
                    ret[half] = []
                ret[half].append((i, j))
        return ret

    def fourSum(self, num, target):
        num = sorted(num)
        tupleHash = self.genHash(num)

        ret = set()

        for half1 in sorted(tupleHash):
            half2 = target - half1
            if half2 in tupleHash:
                for tup1 in tupleHash[half1]:
                    for tup2 in tupleHash[half2]:
                        if tup1[1] < tup2[0]:
                            ret.add((
                                num[tup1[0]],
                                num[tup1[1]],
                                num[tup2[0]],
                                num[tup2[1]]
                                ))

        return [ list(t) for t in ret]


if __name__ == "__main__":
    print Solution().fourSum([2,1,0,-1], 2)


