class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = len(nums) - 1
        
        if nums[i] < nums[j]:
            return nums[i]
        elif len(nums) == 1:
            return nums[0]
        
        while i <= j:
            mid = (i+j)//2
            
            if nums[i] > nums[mid]:
                j = mid - 1
                if nums[mid] < nums[j]:
                    return nums[mid]
            else:
                i = mid + 1
                if nums[mid] > nums[i]:
                    return nums[i]