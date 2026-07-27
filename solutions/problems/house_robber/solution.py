class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = []
        
        for i in range(len(nums)):

            if i == 0 :
                dp.append(nums[0])
            elif i == 1:
                dp.append(max(nums[0], nums[1]))
            else:
                dp.append(max(dp[i-1], dp[i-2]+nums[i]))

        return max(dp)