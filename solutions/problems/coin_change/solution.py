class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        coinsdict = {}
        
        def bestOf(amount):
            if amount <= 0:
                return 0

            if coinsdict.get(amount, None) is not None:
                return coinsdict.get(amount)
                
            dp = []
            
            for c in coins:
                balance = amount - c
                if coinsdict.get(balance, None) is not None and coinsdict.get(balance, None) != -1:
                    dp.append(1+ coinsdict.get(balance))
                elif balance == 0:
                    dp.append(1)
                elif balance > 0:
                    best = bestOf(balance)
                    if best != -1:
                        minimumCoins = 1+best
                        dp.append(minimumCoins)

            if dp:
                coinsdict[amount] = min(dp)
                return coinsdict.get(amount)
            else:
                coinsdict[amount] = -1
                return -1

        return bestOf(amount)