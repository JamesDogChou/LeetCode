class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        MaxLen = 0          # The answer
        dictLastAppear = {} # Record each character's last appear position
        lenStr = len(s)
        basePos = 0         # The base position to compute the max length
        for i in xrange(0, lenStr):
            # Check if there is a same character before
            tempCheck = dictLastAppear.get(s[i], None)
            if tempCheck != None:
                # Update the answer if current non-repeat length is longer
                MaxLen = max(MaxLen, i - basePos)
                # Update the current base position to the right-most and non-repeat position
                basePos = max(basePos, tempCheck + 1)
            # Update the character position
            dictLastAppear[s[i]] = i
        # Last Check
        MaxLen = max(MaxLen, lenStr - basePos)
        return MaxLen
