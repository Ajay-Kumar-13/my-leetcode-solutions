class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        
        window_length = len(cardPoints) - k

        s = 0
        min_sum = 0
        total = sum(cardPoints)

        for i in range(window_length):
            s += cardPoints[i]

        min_sum = s
        i = 0
        j = window_length

        while j < len(cardPoints):
            s -= cardPoints[i]
            s += cardPoints[j]
            i += 1
            j += 1
            min_sum = min(s, min_sum)

        return total-min_sum