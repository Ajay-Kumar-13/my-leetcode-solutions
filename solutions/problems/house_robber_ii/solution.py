class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        
        dp = []

        for i in range(len(nums)-1):
            if i == 0:
                dp.append(nums[0])
            elif i == 1:
                dp.append(max(nums[0], nums[1]))
            else:
                dp.append(max(dp[i-1], nums[i]+dp[i-2]))

        dp2 = []

        for i in range(1, len(nums)):
            if i == 1:
                dp2.append(nums[1])
            elif i == 2:
                dp2.append(max(nums[1], nums[2]))
            else:
                dp2.append(max(dp2[i-2], nums[i]+dp2[i-3]))

        if dp2:
            return max(max(dp), max(dp2))
        
        return max(dp)