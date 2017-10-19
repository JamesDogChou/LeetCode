class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # DP[i][j] represents isMatch(s[i:], p[j:])
        lenS = len(s)
        lenP = len(p)
        
        DP = [[False] * (lenP + 1) for i in xrange(lenS + 1)]
        DP[-1][-1] = True
        for i in xrange(lenS, -1, -1):
            for j in xrange(lenP - 1, -1, -1):
                ijMatch = i < lenS and (p[j] == s[i] or p[j] == '.')
                if j+1 < lenP and p[j+1] == '*':
                    DP[i][j] = DP[i][j+2] or (ijMatch and DP[i+1][j])
                else:
                    DP[i][j] = ijMatch and DP[i+1][j+1]
        
        return DP[0][0]
