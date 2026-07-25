class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        def isPossible(k):
            hours = 0
            for pile in piles:
                hours += ((pile + k - 1) // k)
            
            return hours
        
        i = 1
        j = max(piles)
        k = j
        while i <= j:
            mid = (i + j) // 2
            hours = isPossible(mid)
            
            if hours <= h:
                k = min(k, mid)
                j = mid - 1
            else:
                i = mid + 1

        return k 