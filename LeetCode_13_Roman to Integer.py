class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        iterS = 0
        lenS = len(s)
        num = 0
        
        while iterS < lenS:
            if s[iterS] == 'M':
                num += 1000
            else:
                break
            iterS += 1
        else:
            return num              # return when iterS >= lenS
        
        Done = False
        if s[iterS] == 'D':
            num += 500
            iterS += 1
        elif s[iterS] == 'C':
            num += 100
            iterS += 1
            if iterS < lenS:
                if s[iterS] == 'D':
                    iterS += 1
                    num += 300
                    Done = True
                elif s[iterS] == 'M':
                    iterS += 1
                    num += 800
                    Done = True
            else:
                return num
        if not Done:
            while iterS < lenS:
                if s[iterS] == 'C':
                    num += 100
                else:
                    break
                iterS += 1
            else:
                return num
        if iterS >= lenS:
            return num
        
        Done = False
        if s[iterS] == 'L':
            num += 50
            iterS += 1
        elif s[iterS] == 'X':
            num += 10
            iterS += 1
            if iterS < lenS:
                if s[iterS] == 'L':
                    iterS += 1
                    num += 30
                    Done = True
                elif s[iterS] == 'C':
                    iterS += 1
                    num += 80
                    Done = True
            else:
                return num
        if not Done:
            while iterS < lenS:
                if s[iterS] == 'X':
                    num += 10
                else:
                    break
                iterS += 1
            else:
                return num
        if iterS >= lenS:
            return num

        dictOneToTen = {'': 0, 'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9, 'X': 10}
        return num + dictOneToTen.get(s[iterS:], 0)
        