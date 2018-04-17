class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        lenH = len(height)
        if lenH < 2:
            return 0
        currentDistance = itEnd = lenH - 1
        if height[0] > height[itEnd]:
            maxCon = height[itEnd] * currentDistance
            itEnd -= 1
            itStart = 0
            checkStart = False
        else:
            maxCon = height[0] * currentDistance
            itStart = 1
            checkStart = True
        currentDistance -= 1
        while currentDistance:
            if checkStart:      # check iterator-start
                if height[itStart] > height[itStart-1]:
                    if height[itStart] > height[itEnd]:
                        tempCon = height[itEnd] * currentDistance
                        itEnd -= 1
                        checkStart = False
                    else:
                        tempCon = height[itStart] * currentDistance
                        itStart += 1
                    maxCon = tempCon if tempCon > maxCon else maxCon
                else:
                    itStart += 1
            else:               # check iterator-end
                if height[itEnd] > height[itEnd+1]:
                    if height[itEnd] > height[itStart]:
                        tempCon = height[itStart] * currentDistance
                        itStart += 1
                        checkStart = True
                    else:
                        tempCon = height[itEnd] * currentDistance
                        itEnd -= 1
                    maxCon = tempCon if tempCon > maxCon else maxCon
                else:
                    itEnd -= 1
            currentDistance -= 1
        return maxCon