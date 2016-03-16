class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        buckets = {}
        for index in xrange(1, len(nums)):
            buckets[nums[index]] = index
        for index in xrange(0, len(nums)):
            index2 = buckets.get(target - nums[index], 0)
            if index2 > 0:
                return [index, index2]
        return None
        