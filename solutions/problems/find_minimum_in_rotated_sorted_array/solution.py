class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1

        while i < j:
            mid = (i+j)//2

            if nums[mid-1] > nums[mid]:
                return nums[mid]

            if nums[i] < nums[mid]:
                i = mid
            else:
                j = mid
        
        if nums[0] > nums[len(nums)-1]:
            return nums[len(nums)-1]
        else:
            return nums[0]