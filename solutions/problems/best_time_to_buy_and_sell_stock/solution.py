class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        i = len(prices)

        if i < 2:
            return 0

        rightHighest = [prices[i - 1]]
       

        for j in range(i-2, -1, -1):
            if prices[j] > rightHighest[i-j-2]:
                rightHighest.append(prices[j])
            else:
                rightHighest.append(rightHighest[i-j-2])

        rightHighest.reverse()

        profit = 0

        for i in range(len(prices)):
            profit = max(profit, (rightHighest[i] - prices[i]))

        return profit

