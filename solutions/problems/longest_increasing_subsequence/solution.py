class Solution:
    def lengthOfLIS(self, nums):
        
        dp = []
        for i in range(len(nums)):
            count = 0
            for j in range(i-1, -1, -1):
                if nums[j] < nums[i]:
                    count = max(count, dp[j])
                    
            dp.append(1 + count)
            
        return max(dp)