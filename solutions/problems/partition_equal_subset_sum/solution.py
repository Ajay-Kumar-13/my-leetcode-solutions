class Solution:

    def findWays(self, ind, target, nums, dp):

        if dp[ind][target] != -1:
            return dp[ind][target]

        if ind == 0:
            if nums[ind] == target:
                return True

            return False

        if target == 0:
            return True

        found = self.findWays(ind-1, target, nums, dp)
        if found:
            return True
        pick = False
        if nums[ind] <= target:
            pick = self.findWays(ind-1, target-nums[ind], nums, dp)


        dp[ind][target] = pick
        return pick



    def canPartition(self, nums):
        
        totalSum = sum(nums)
        if totalSum % 2 != 0:
            return False

        l = len(nums)

        target = (totalSum // 2)

        dp = [[False] * (target+1) for _ in range(l)]

        for i in range(l):
            dp[i][0] = True

        if nums[0] <= target:
            dp[0][nums[0]] = True

        for i in range(1, l):
            for j in range(1, target+1):

                found = dp[i-1][j]
                pick = False
                if nums[i] <= j:
                    pick = dp[i-1][j-nums[i]]

                dp[i][j] = pick or found

        return dp[l-1][target]