class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
    
        dp = [1]
        
        for i in range(1, len(nums)):
            j = i-1
            total = 1
            while j >= 0:
                if nums[i] > nums[j]:
                    total = max(total, 1 + dp[j])
                j -= 1
            dp.append(total)
        
        return max(dp)