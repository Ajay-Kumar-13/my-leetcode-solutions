class Solution(object):
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        
        def smallElementsBeforeMid(m, n, mid):
            total = 0
            
            for i in range(1, m+1):
                total += min(n, mid//i)
            
            return total
        
        i = 1
        j = m*n
        
        knum = float('inf')
        
        while i <= j:
            mid = (i+j) // 2
            
            elementsBeforeMid = smallElementsBeforeMid(m, n, mid)

            if elementsBeforeMid >= k: 
                knum = min(mid, knum)
                j = mid - 1
            else:
                i = mid + 1
                
        return knum