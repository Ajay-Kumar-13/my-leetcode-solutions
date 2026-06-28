class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        j = len(nums) - 1

        while j > 0 and nums[j] <= nums[j-1]:
            j -= 1

        if j == 0:
            nums.sort()
        else:
            i = len(nums) - 1
            while nums[i] <= nums[j-1] and i > 0:
                i -= 1

            nums[j-1], nums[i] = nums[i], nums[j-1]
            nums[j:] = reversed(nums[j:])
    

        return nums