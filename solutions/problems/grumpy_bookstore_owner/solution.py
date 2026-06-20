class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """
        # Unsatisfied In Window
        USIW = 0 
        # Satisfied In Total
        SIT = 0
        # Max Unsatisfied
        MXUS = 0

        for i in range(minutes):
            if grumpy[i] == 0:
                SIT += customers[i]
            elif grumpy[i] == 1:
                USIW += customers[i]

        MXUS = USIW
        i = 1
        j = minutes
        while j < len(customers):
            if grumpy[i-1] == 1:
                USIW -= customers[i-1]
            if grumpy[j] == 1:
                USIW += customers[j]
            if grumpy[j] == 0:
                SIT += customers[j]
            MXUS = max(MXUS, USIW)
            j += 1
            i += 1

        return SIT + MXUS