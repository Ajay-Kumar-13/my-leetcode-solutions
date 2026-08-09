class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        def findWays(ind, target, dp):
            if ind == len(nums):
                if target == 0:
                    return 1
                return 0

            if dp[ind][target] != -1:
                return dp[ind][target]

            pick = 0
            if nums[ind] <= target:
                pick = findWays(ind+1, target-nums[ind], dp)
            
            notPick = findWays(ind+1, target, dp)
            
            dp[ind][target] = pick+notPick

            return pick+notPick

        diff = sum(nums)-target

        if diff % 2 != 0 or diff < 0 or sum(nums) < target:
            return 0

        target = (diff)//2

        dp = [[-1]*(target+1) for _ in range(len(nums))]

        return findWays(0, target, dp)