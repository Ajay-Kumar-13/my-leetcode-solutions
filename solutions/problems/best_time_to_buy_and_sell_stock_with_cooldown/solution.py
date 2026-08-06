class Solution:

    def getMaxProfit(self, ind, prices, iCanBuy, dp):
        if ind >= len(prices):
            return 0

        if dp[ind][iCanBuy] != -1:
            return dp[ind][iCanBuy]

        if iCanBuy:
            val =  max(self.getMaxProfit(ind+1, prices, False, dp), self.getMaxProfit(ind+1, prices, True, dp))
            dp[ind][iCanBuy] = val
            return val
        else:
            val = max(
                (prices[ind] - prices[ind-1]) + self.getMaxProfit(ind+2, prices, True, dp),
                (prices[ind] - prices[ind-1]) + self.getMaxProfit(ind+1, prices, False, dp)
            )
            dp[ind][iCanBuy] = val
            return val



    def maxProfit(self, prices: List[int]) -> int:

        dp = [[-1]*2 for _ in range(len(prices))]
        
        return self.getMaxProfit(0, prices, True, dp)