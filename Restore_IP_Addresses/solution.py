class Solution:
    # @param s, a string
    # @return a list of strings

    def converToNum(self, partial_s):
        if len(partial_s) > 1 and partial_s[0] == '0':
            return None
        sub_int = int(partial_s)
        if 0 <= sub_int and sub_int <= 255:
            return sub_int
        return None

    def restoreIpAddresses(self, s):
        dp = {}
        for j in range(len(s)):

            if j < 3:
                sub_int = self.converToNum(s[:j+1])
                if not sub_int == None:
                    dp[j] = [[str(sub_int)]]

            for i in range(j-2,j+1):
                if i < 0:
                    continue

                sub_int = self.converToNum(s[i:j+1])

                if(not sub_int ==None):
                    mem_ints_array = dp.get(i-1)
                    if not mem_ints_array == None:
                        for mem_ints in mem_ints_array:
                            if len(mem_ints) <= 3:
                                if not dp.has_key(j):
                                    dp[j] = []
                                new_mem_ints = [v for v in mem_ints]
                                new_mem_ints.append(str(sub_int))
                                dp[j].append(new_mem_ints)

        all_ips = []
        last = dp.get(len(s)-1)
        if not last == None:
            for mem_ints in last:
                if len(mem_ints) == 4:
                    all_ips.append( ".".join(mem_ints) )
            return all_ips
        else:
            return []
if __name__ == "__main__":
    print Solution().restoreIpAddresses("25525511135")
    print Solution().restoreIpAddresses("0000")
    print Solution().restoreIpAddresses("010010")
