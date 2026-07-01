class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        i = 0
        j = min(len(nums1), len(nums2))
        
        if len(nums1) > len(nums2):
            nums2, nums1 = nums1, nums2
            
        n = len(nums1) + len(nums2)
        # ceiling the value (a+b-1)//b
        l = (n + 1)//2
            

        
        while i <= j:
            
            l1 = -float('inf')
            l2 = -float('inf')
            r1 = float('inf')
            r2 = float('inf')
        
            mid1 = (i+j)//2
            mid2 = l - mid1
            
            if mid1 - 1 >= 0:
                l1 = nums1[mid1-1]
                
            if mid1 < len(nums1):
                r1 = nums1[mid1]
                
            if mid2-1 >= 0:
                l2 = nums2[mid2-1]
                
            if len(nums2) > mid2:
                r2 = nums2[mid2]
            
            if l1 <= r2 and l2 <= r1:
                break
            elif l2 > r1:
                i = mid1 + 1
            else:
                j = mid1 - 1
                
        if n % 2 == 0:
            return float((max(l1, l2) + min(r1, r2)) / 2)
        else:
            return float(max(l1, l2))
