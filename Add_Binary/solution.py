class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        a_list = [ e for e in reversed(list(a))]
        b_list = [ e for e in reversed(list(b))]

        if len(a_list) < len(b_list):
            a_list, b_list = b_list, a_list

        out_line = ""
        tmp_bit = '0'
        for a_i in range(len(a_list)):
            if a_i < len(b_list):
                b_bit = b_list[a_i]
            else:
                b_bit = '0'
            a_bit = a_list[a_i]

            count = int(a_bit) + int(b_bit) + int(tmp_bit)
            if count == 3:
                tmp_bit = '1'
                cur_bit = '1'
            elif count == 2:
                tmp_bit = '1'
                cur_bit = '0'
            elif count == 1:
                tmp_bit = '0'
                cur_bit = '1'
            elif count == 0:
                tmp_bit = '0'
                cur_bit = '0'
            out_line = cur_bit + out_line
        if tmp_bit == '1':
            out_line = '1' + out_line

