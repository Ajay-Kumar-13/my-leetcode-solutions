class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        
        s = sum(nums)

        total_sum = s - x

        if total_sum < 0:
            return -1

        i  = 0
        j = 0
        s = 0
        max_len = -1

        while i < len(nums):
            if s >= total_sum:
                if s == total_sum:
                    max_len = max(max_len, j-i)
                s -= nums[i]
                i += 1
            elif j < len(nums):
                s += nums[j]
                j += 1
            else:
                i += 1
            
                
        if s == total_sum:
            max_len = max(max_len, j-i)
            
        if max_len == -1:
            return max_len
            
        return len(nums) - max_len