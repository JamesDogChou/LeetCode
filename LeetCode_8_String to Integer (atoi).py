class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        #import sys
        max_int = 2147483647 # sys.maxint
        min_int = -max_int - 1
        #print max_int, min_int
        len_str = len(str)
        if len_str == 0:
            return 0
        sign = 1
        start_pos = 0
        while start_pos < len_str and str[start_pos].isspace():
            start_pos += 1
        if not str[start_pos].isdigit():
            if str[start_pos] == '-':
                sign = -1
            elif str[start_pos] == '+':
                pass # sign = 1
            else:
                return 0
            start_pos += 1
        #print start_pos
        ans = 0
        i = start_pos
        while i < len_str:
            if not str[i].isdigit():
                return sign * ans
            current_digit = int(str[i])
            if sign == 1 and ans > (max_int - current_digit)/10:   # larger than max_int
                return max_int  
            elif sign == -1 and ans > (-min_int - current_digit)/10: # smaller than min_int
                return min_int
            else:
                ans = ans*10 + current_digit
            i += 1
        return sign * ans
        