class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        stringLen = len(s)
        if stringLen == 0: 
            return ""
        maxLen = 1
        maxIndex = 0
        dictOdd = {}    # for the palindromic substrings whose length is odd
        dictEven = {}   # for the palindromic substrings whose length is even
        
        # initialize  dictOdd and dictEven
        for i in xrange(stringLen):
            dictOdd[i] = 0
        hasFound = 0
        for i in xrange(stringLen-1):
            if s[i] == s[i+1]:
                dictEven[i] = 0
                if not hasFound:
                    hasFound = 1
                    maxLen = 2
                    maxIndex = i
        
        # Find as longer as every palindromic substring can be
        while 1:
            hasFound = 0
            for key, value in dictOdd.items():
                l = key - value - 1
                r = key + value + 1
                if l >= 0 and r < stringLen and (s[l] == s[r]):
                    dictOdd[key] = value + 1
                    if not hasFound:
                        hasFound = 1
                        maxIndex = key
                        maxLen = value*2 + 3 # (value+1)*2 + 1
                else:
                    del dictOdd[key]
            #print dictOdd
            hasFound = 0
            for key, value in dictEven.items():
                l = key - value - 1
                r = key + value + 2
                if l >= 0 and r < stringLen and (s[l] == s[r]):
                    dictEven[key] = value + 1
                    if not hasFound:
                        hasFound = 1
                        maxIndex = key
                        maxLen = value*2 + 4 # (value+1)*2 + 2
                else:
                    del dictEven[key]
            #print dictEven
            if len(dictOdd)==0 and len(dictEven)==0:
                break
        if maxLen%2:
            r = (maxLen - 1) / 2
            #print maxIndex, r
            return s[maxIndex-r:maxIndex+r+1]
        else:
            r = maxLen / 2 - 1
            #print maxIndex, r
            return s[maxIndex-r:maxIndex+r+2]
            