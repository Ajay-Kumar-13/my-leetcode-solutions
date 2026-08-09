class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [[-1]*(amount+1) for _ in range(len(coins))]

        def minimumCoins(ind, coins, amount):
    
            if ind == len(coins):
                return float('inf')
            
            if amount == 0:
                return 0

            if dp[ind][amount] != -1:
                return dp[ind][amount]
                
            balance = amount - coins[ind]
                
            take = float('inf')
            if balance >= 0:
                take = 1 + minimumCoins(ind, coins, balance)
            
            notTake = minimumCoins(ind+1, coins, amount)

            dp[ind][amount] = min(take, notTake)
            
            return min(take, notTake)

        totalCoins = minimumCoins(0, coins, amount)
        
        if totalCoins != float('inf'):
            return totalCoins

        return -1