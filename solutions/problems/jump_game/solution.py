class Solution:
    def canJump(self, nums):
                
        dp = []

        for i in range(len(nums)):
            
            if dp and dp[i-1] < i:
                return False

            if not dp:
                dp.append(nums[i]+i)
            else:
                dp.append(max(nums[i]+i, dp[i-1]))

        return True
