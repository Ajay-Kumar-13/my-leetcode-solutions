class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        i = 0
        j = len(nums) - 1
        
        while i <= j:
            mid = (i+j) // 2
            
            if mid == 0 or mid == len(nums) -1 or i == j:
                return nums[mid]
            
            if mid % 2 == 0:
                if nums[mid] == nums[mid+1]:
                    i = mid + 1
                else:
                    j = mid
            else:
                if nums[mid] != nums[mid+1]:
                    i = mid + 1
                else:
                    j = mid
        
        return nums[mid]
        