class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        frequency = {}
        i = 0
        
        j = 0
        
        maxi = 0
        
        while j < len(nums):
            
            if nums[j] != 0:
                frequency[1] = frequency.get(1, 0)+1
            
            j += 1
            
            if (j-i) - frequency.get(1, 0) > k:
                if nums[i] == 1:
                    frequency[nums[i]] = frequency.get(1, 0) - 1
                i += 1
            else:
                maxi = max(maxi, (j-i))
        
        return maxi