class Solution:
    def numSquares(self, n: int) -> int:

        dp = {}
        
        def totalSquares(n):
            
            if n == 0:
                return 0
            
            if n == 1:
                return 1

            if dp.get(n, None) is not None:
                return dp.get(n)
        
            total = float('inf')
        
            i = 1
            j = 1
            while j <= n:
                ps = totalSquares(n-j)
                dp[n-j] = ps
                total = min(total, 1+ps)
        
                i += 1
                j = i*i
            
            return total
    
        return totalSquares(n)