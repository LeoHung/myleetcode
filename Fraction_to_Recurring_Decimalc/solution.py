class Solution:
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        isNeg = False
        if numerator < 0 :
            numerator = - numerator 
            isNeg = not isNeg
        if denominator < 0:
            denominator = - denominator
            isNeg = not isNeg

        if numerator == 0:
            return "0"

        integer = numerator/ denominator
        numerator = numerator % denominator

        ret_str = ""
        if isNeg:
            ret_str += "-"

        ret_str += str(integer)
        
        if numerator != 0: 
            ret_str += "."

            digit_list = []
            remainder_hash = {}
            d_i = 0
            while True:
                remainder_hash[numerator] = d_i

                digit_list.append(str((numerator*10)/ denominator))
                
                numerator = (numerator * 10 ) % denominator
                d_i += 1 

                if numerator in remainder_hash or numerator == 0:
                    break

            if numerator == 0:
                ret_str += "".join(digit_list)
            else:
                ret_str = ret_str + "".join(digit_list[:remainder_hash[numerator]]) + "(" + "".join(digit_list[remainder_hash[numerator]:d_i]) + ")"

        return ret_str

if __name__ == "__main__":
    print Solution().fractionToDecimal(1, 2)
    print Solution().fractionToDecimal(2, 1)
    print Solution().fractionToDecimal(2, 3)
    print Solution().fractionToDecimal(1, 6)
    print Solution().fractionToDecimal(-50, 8)