class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        def isPossibleInDays(bloomDays, days, m, k):
            if m * k > len(bloomDays):
                return False
            
            adjacentFlowers = k
            bouquet = 0
            for day in bloomDays:
                if day <= days:
                    adjacentFlowers -= 1
                elif adjacentFlowers != 0:
                    adjacentFlowers = k
                
                if adjacentFlowers == 0:
                    bouquet += 1
                    adjacentFlowers = k
                    
                if bouquet == m:
                    return True
                
            return False
                
        
        i = min(bloomDay)
        j = max(bloomDay)
        
        minDaysRequired = float('inf')
        
        while i <= j:
            mid = (i+j)//2
            if isPossibleInDays(bloomDay, mid, m, k):
                minDaysRequired = min(minDaysRequired, mid)
                j = mid - 1
            else:
                i = mid + 1
        
        if minDaysRequired == float('inf'):
            return -1
            
        return minDaysRequired