class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        
        total_sum = sum(cardPoints)

        window_length = len(cardPoints) - k

        

        score = 0
        for i in range(window_length):
            score += cardPoints[i]

        i = 1
        j = window_length
        min_score = score
        while j < len(cardPoints):
            score -= cardPoints[i-1]
            score += cardPoints[j]

            min_score = min(min_score, score)
            j += 1
            i += 1

        return total_sum - min_score