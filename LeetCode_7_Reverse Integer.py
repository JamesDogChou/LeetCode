class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ans = 0
        sign = 1
        if x < 0:
            x *= -1
            sign = -1
        try:
            while x != 0:
                ans = ans*10 + x%10
                x /= 10
        except:
            return 0
        return ans * sign if ans<2147483648 else 0