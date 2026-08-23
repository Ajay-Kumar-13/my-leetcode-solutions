class Solution:
    def findPeakElement(self, nums):
        
        i = 0
        j = len(nums) - 1

        while i < j:
            mid = (i+j) // 2

            if nums[mid+1] > nums[mid]:
                i = mid + 1
            elif mid-1 >= 0 and nums[mid-1] < nums[mid]:
                return mid
            else:
                j = mid

        return i