class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        lenS = len(s)
        lenP = len(p)
        return self.DFS(s, lenS, p, lenP)
        
    def DFS(self, targetStr, lenTarget, regularExp, lenRegular):
        if targetStr == regularExp:
            return True
        elif lenRegular == 0:
            if lenTarget == 0:
                return True
            else:
                return False
        elif lenTarget == 0:
            # check if regularExp can be null string
            while regularExp:
                if regularExp[-1] == '*':
                    if len(regularExp) < 2:
                        return False
                    else:
                        regularExp = regularExp[:-2]
                else:
                    return False
            return True
        elif (targetStr[-1] == regularExp[-1] or regularExp[-1] == '.'):
            if self.DFS(targetStr[:-1], lenTarget-1, regularExp[:-1], lenRegular-1):
                return True
            else:
                return False
        elif regularExp[-1] == '*' and lenRegular > 1:
            # handle recursive of regular expression *
            if self.DFS(targetStr, lenTarget, regularExp[:-2], lenRegular-2):
                return True
            tempChar = regularExp[-2]
            if tempChar == '.':
                '''
				# I think '.' can only represent the same char when it's before '*'
                tempTarget = targetStr[-1]
                while lenTarget and targetStr[-1] == tempTarget:
                    targetStr = targetStr[:-1]
                    lenTarget -= 1
                    if self.DFS(targetStr, lenTarget, regularExp[:-2], lenRegular-2):
                        return True
                '''
                while lenTarget:
                    targetStr = targetStr[:-1]
                    lenTarget -= 1
                    if self.DFS(targetStr, lenTarget, regularExp[:-2], lenRegular-2):
                        return True
            else:
                while lenTarget and targetStr[-1] == tempChar:
                    targetStr = targetStr[:-1]
                    lenTarget -= 1
                    if self.DFS(targetStr, lenTarget, regularExp[:-2], lenRegular-2):
                        return True
            return False
        else:
            return False
        