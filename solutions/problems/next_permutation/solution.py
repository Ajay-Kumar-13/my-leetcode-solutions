class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        if len(nums) < 2:
            return nums
        
        i = len(nums) - 1

        while nums[i-1] >= nums[i] and i > 0:
            i -= 1

        if i == 0:
            nums.sort()
            return nums
        else:
            i -= 1
            j = i + 1

            swap = j

            diff = float('inf')

            while j < len(nums):

                d = nums[j] - nums[i]

                if diff >= d and d > 0:
                    swap = j
                    diff = d

                j = j+ 1

            nums[i], nums[swap] = nums[swap], nums[i] 
            
            j = len(nums)-1
            i += 1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            
        return nums