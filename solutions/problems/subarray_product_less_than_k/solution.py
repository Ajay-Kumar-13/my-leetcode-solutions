class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        total = 1
        i = 0
        ans = 0
        
        for j,n in enumerate(nums):
            total *= n
            if total < k:
                ans += (j-i+1)
            else:
                while total >= k and i < j:
                    total //= nums[i]
                    i += 1
                if total < k:
                    ans += (j-i+1)

        return ans