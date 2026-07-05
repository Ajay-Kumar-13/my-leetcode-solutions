class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        total = 0
        ans = 0
        fliped = 0
        i = 0
        for j in range(len(nums)):
            
            if nums[j] == 0:
                fliped += 1
            
            total += 1
            
            if fliped <= k:
                ans = max(ans, total)

            while fliped > k:
                if nums[i] == 0:
                    fliped -= 1
                total -= 1
                i += 1
        
        return ans