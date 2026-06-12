class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i  = 0
        j = i + 1

        while i < j and j < len(nums):
            k = i 
            if nums[i] > nums[j] :
                nums[i], nums[j] = nums[j], nums[i]

            while k >= 1 and nums[k] < nums[k-1]:
                nums[k-1], nums[k] = nums[k], nums[k-1]
                k = k -1
            
            i += 1
            j = i+1

        return nums