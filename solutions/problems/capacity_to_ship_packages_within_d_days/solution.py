class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        
        def isCapable(weight, days):
            current_day = 0
            for weigh in weights:
                
                if weigh > weight:
                    return False
                
                current_day += weigh
                
                if current_day > weight:
                    days -= 1
                    current_day = weigh
                    
                if days == 0:
                    return False
            
            return True
        
        totalWeight = sum(weights)
        
        i = 1
        j = totalWeight
        
        minWeight = float('inf')
        
        while i <= j:
            weight = (i+j)//2
            if isCapable(weight, days):
                minWeight = min(minWeight, weight)
                j = weight - 1
            else:
                i = weight + 1

        return minWeight