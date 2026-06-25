class StockSpanner(object):

    def __init__(self):
    
        self.stack = []
        
    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        ans = 1
        while len(self.stack) > 0 and price >= self.stack[-1][0]:
            obj = self.stack.pop()
            ans += obj[1]
            
        self.stack.append((price, ans))
        
        return ans
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)