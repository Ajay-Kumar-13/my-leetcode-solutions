class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        def kokoCanFinishAllBananas(k, h):
            
            for pile in piles:
                h -= ((pile + k - 1) // k)

            if h < 0:
                return False

            return True
        
        r = max(piles)
        l = 1
        finishedInHours = r

        while l <= r:
            k = (l+r) // 2

            if kokoCanFinishAllBananas(k, h):
                finishedInHours = min(finishedInHours, k)
                r = k - 1
            else:
                l = k + 1

        return finishedInHours