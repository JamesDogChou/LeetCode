class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        elif x<10:
            return True
        copy_x = x
        y = 0
        while copy_x != 0:
            y = 10*y + copy_x%10
            copy_x /= 10
        if y == x:
            return True
        else:
            return False