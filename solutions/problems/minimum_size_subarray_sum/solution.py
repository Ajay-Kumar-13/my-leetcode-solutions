class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        mini = float('inf')
        i  = 0
        j = 0
        length = len(nums)
        total = 0

        while j < length: 
            
            total += nums[j]
            j += 1    
                
            while i < j and total >= target:
                mini = min(j-i, mini)
                total -= nums[i]
                i += 1

        if mini == float('inf'):
            return 0
        else:
            return mini