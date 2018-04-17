class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        if num >= 3000:
            outputStr = 'MMM'
        elif num >= 2000:
            outputStr = 'MM'
        elif num >= 1000:
            outputStr = 'M'
        else:
            outputStr = ''
        
        num = num % 1000
        num3 = num / 100
        if num3 == 1:
            outputStr += 'C'
        elif num3 == 2:
            outputStr += 'CC'
        elif num3 == 3:
            outputStr += 'CCC'
        elif num3 == 4:
            outputStr += 'CD'
        elif num3 == 5:
            outputStr += 'D'
        elif num3 == 6:
            outputStr += 'DC'
        elif num3 == 7:
            outputStr += 'DCC'
        elif num3 == 8:
            outputStr += 'DCCC'
        elif num3 == 9:
            outputStr += 'CM'
        
        num = num % 100
        num2 = num / 10
        if num2 == 1:
            outputStr += 'X'
        elif num2 == 2:
            outputStr += 'XX'
        elif num2 == 3:
            outputStr += 'XXX'
        elif num2 == 4:
            outputStr += 'XL'
        elif num2 == 5:
            outputStr += 'L'
        elif num2 == 6:
            outputStr += 'LX'
        elif num2 == 7:
            outputStr += 'LXX'
        elif num2 == 8:
            outputStr += 'LXXX'
        elif num2 == 9:
            outputStr += 'XC'
        
        num1 = num % 10
        if num1 == 1:
            outputStr += 'I'
        elif num1 == 2:
            outputStr += 'II'
        elif num1 == 3:
            outputStr += 'III'
        elif num1 == 4:
            outputStr += 'IV'
        elif num1 == 5:
            outputStr += 'V'
        elif num1 == 6:
            outputStr += 'VI'
        elif num1 == 7:
            outputStr += 'VII'
        elif num1 == 8:
            outputStr += 'VIII'
        elif num1 == 9:
            outputStr += 'IX'
            
        return outputStr