class Solution:
    def jump(self, nums):
        
        if len(nums) <= 1:
            return 0
                        
        dp = []
        for i in range(len(nums)-1):

            if dp and dp[i-1] >= len(nums)-1:
                break

            if not dp:
                dp.append(nums[i]+i)
            else:
                dp.append(max(nums[i]+i, dp[i-1]))
        
        
        return 1 + self.jump(nums[:len(dp)])