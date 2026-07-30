class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [(nums[0], nums[0])]

        maxi = nums[0]

        for i in range(1, len(nums)):

            maxProd = dp[i-1][0]*nums[i]
            minProd = dp[i-1][1]*nums[i]

            t = (max(maxProd, minProd, nums[i]), min(maxProd, minProd, nums[i]))
            
            dp.append(t)

            maxi = max(maxi, max(maxProd, minProd, nums[i]))

        return maxi