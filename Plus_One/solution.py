class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        num_str = "".join([str(d) for d in digits ])
        num = int(num_str) +1
        num_str = str(num)
        return [ int(s) for s in list(num_str)]
