class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        
        total = 0
        minLength = float('inf')
        i = 0
        
        for j in range(len(nums)):
            total += nums[j]
                
            while total >= target:
                minLength = min(minLength, j+1-i) 
                total -= nums[i]
                i += 1
                
        if minLength == float('inf'):
            return 0 

        return minLength