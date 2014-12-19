class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        tmp_1 = [int(e) for e in version1.split(".")]
        tmp_2 = [int(e) for e in version2.split(".")]

        l = max([len(tmp_1), len(tmp_2)])

        for i in range(l):
            if i < len(tmp_1):
                v1 = tmp_1[i]
            else:
                v1 = 0

            if i < len(tmp_2):
                v2 = tmp_2[i]
            else:
                v2 = 0

            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1 

        return 0

if __name__ == "__main__":
    print Solution().compareVersion("0.1.2", "1.1")
    print Solution().compareVersion("1.1", "0.1.0")
    print Solution().compareVersion("0.1", "0.1")
