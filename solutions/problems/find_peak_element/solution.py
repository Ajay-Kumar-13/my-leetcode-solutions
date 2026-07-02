class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        i = 0
        j = len(nums)-1
        
        while i <= j:
            mid = (i+j)//2
            
            if mid + 1 >= len(nums):
                break
            
            if nums[mid+1] > nums[mid]:
                i = mid + 1
            else:
                j = mid - 1
                
        return i