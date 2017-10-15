class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        listRow = []
        for i in xrange(numRows):
            listRow.append([])
        slen = len(s)
        p = 0 # now in which row
        inc = 1 # 1=increase; -1=decrease
        for i in xrange(slen):
            listRow[p].append(s[i])
            p = p + inc
            if p == numRows:
                p = p - 2
                inc = -1
            elif p == -1:
                p = 1
                inc = 1
        ans = ""
        for i in xrange(numRows):
            for j in xrange(len(listRow[i])):
                ans += listRow[i][j]
        return ans
        