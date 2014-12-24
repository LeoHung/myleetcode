class Solution:
    # @return a string
    def convertToTitle(self, num):
        characters = [
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
        ]

        ret = ""
        while True:
            num -= 1
            ret = characters[ num % 26 ] + ret
            num = num / 26

            if num == 0:
                break
        return ret 

if __name__ == "__main__":
    for i in range(1, 100):
        print Solution().convertToTitle(i)
        