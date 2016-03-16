class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        MaxLen = 0
        dictLastAppear = {}
        lenStr = len(s)
        for i in xrange(0, lenStr):
            tempCheck = dictLastAppear.get(s[i], -1)
            if tempCheck > 0:
                for k, v in dictLastAppear.iteritems():
                    if v >= 0 and v < tempCheck:
                        dictLastAppear[k] = -1
                        tempMax = i - v
                        if tempMax > MaxLen:
                            MaxLen = tempMax
            dictLastAppear[s[i]] = i
                        
        
        for k, v in dictLastAppear.iteritems():
            if v >= 0:
                finalLen = lenStr - v
            else:
                continue
            if finalLen > MaxLen:
                MaxLen = finalLen
        
        return MaxLen