class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)
        totalLen = len1 + len2
        if totalLen%2:
            return self.findKth(nums1, len1, nums2, len2, (totalLen+1)/2)
        else:
            return float(self.findKth(nums1, len1, nums2, len2, totalLen/2) + self.findKth(nums1, len1, nums2, len2, totalLen/2 + 1))/2
    def findKth(self, nums1, m, nums2, n, k):
        # Find Kth smallest element in {nums1+nums2}
        if m > n: # always let nums1 be the shorter one
            return self.findKth(nums2, n, nums1, m, k)
        elif m == 0:
            #print 'k = ', k
            #print 'return ', nums2[k-1]
            return nums2[k-1]
        elif k == 1:
            #print 'return ', min(nums1[0] ,nums2[0])
            return min(nums1[0] ,nums2[0])
        # Trying to remove about k/2 numbers of these two number lists
        pa = min(int((k+1)/2), m)
        pb = k - pa
        if nums1[pa-1] < nums2[pb-1]:
            #print 'nums1[pa:m] = ', nums1[pa:m]
            return self.findKth(nums1[pa:m], m-pa, nums2, n, k-pa)
        elif nums1[pa-1] > nums2[pb-1]:
            #print 'nums2[pb:n] = ', nums2[pb:n]
            return self.findKth(nums1, m, nums2[pb:n], n-pb, k-pb)
        else: # nums1[pa-1] = nums2[pb-1]
            #print 'return ', nums1[pa-1]
            return nums1[pa-1]