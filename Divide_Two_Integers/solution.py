class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        if divisor == 0:
            return (1 << 31) - 1 

        if dividend < 0:
            dvd_sign = - 1 
            dividend = - dividend
        else:
            dvd_sign = 1

        if divisor < 0:
            dvs_sign = - 1
            divisor = - divisor
        else:
            dvs_sign = 1

        quotient = 0

        while dividend >= divisor:
            tmp_divisor = divisor
            tmp_i = 1

            while (tmp_divisor << 1) <= dividend:
                tmp_divisor = tmp_divisor << 1 
                tmp_i = tmp_i << 1 

            dividend -= tmp_divisor
            quotient += tmp_i



        if (dvd_sign < 0 and dvs_sign > 0) or (dvd_sign > 0 and dvs_sign < 0):
            return - quotient
        else:
            if quotient >= ((1 << 31) -1):
                return ((1 << 31) -1)
            else:
                return quotient

if __name__ == "__main__":
    print Solution().divide(1 ,1)
    print Solution().divide(-2147483648 ,-1)