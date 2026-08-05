class Solution:

    def findWays(self, ind, target, nums, dp):

        if dp[ind][target] != -1:
            return dp[ind][target]

        if ind == 0:
            if target == 0 and nums[0] == 0:
                dp[ind][target] = 2
                return 2
            if target == nums[ind] or target == 0:
                dp[ind][target] = 1
                return 1
            return 0 

        notPick = self.findWays(ind-1, target, nums, dp)
        pick = 0
        if (nums[ind] <= target):
            pick = self.findWays(ind-1, target-nums[ind], nums, dp)

        dp[ind][target] = notPick+pick
        return notPick+pick


    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        diff = sum(nums)-target

        target = diff//2

        if diff < 0 or diff % 2 != 0:
            return 0

        l = len(nums)

        dp = [[0]*(target+1) for _ in range(l)]

        for i in range(l):
            dp[i][0] = 1

        if nums[0] == 0:
            dp[0][0] = 2
        else:
            dp[0][0] = 1

        if nums[0] != 0 and nums[0] <= target:
            dp[0][nums[0]] = 1

        for ind in range(1, l):
            for j in range(target+1):

                notPick = dp[ind-1][j]
                pick = 0
                if (nums[ind] <= j):
                    pick = dp[ind-1][j-nums[ind]]

                dp[ind][j] = notPick+pick
        
        return dp[l-1][target]