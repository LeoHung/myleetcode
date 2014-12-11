class Solution:
    # @return an integer
    def reverse(self, x):
        neg = False
        if x < 0:
            neg = True
            x = -x

        num = int("".join([e for e in reversed(list(str(x)))]))

        if neg :
            if num >= 2** 31:
                return 0
            return -num
        else:
            if num >= 2** 31:
                return 0
            else:
                return num
