class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        if len(s) < 1:
            return 1
        
        i = 0
        j = 0

        frequency = {}
        maxFrequency = 0
        maxLength = 0

        while j < len(s):
            window = j - i + 1
            frequency[s[j]] = frequency.get(s[j], 0) + 1
            maxFrequency = max(frequency.get(s[j]), maxFrequency)

            if (window - maxFrequency) <= k:
                maxLength = max(maxLength, window)
            else:
                frequency[s[i]] = frequency.get(s[i]) - 1
                i += 1
                # maxFrequency = max(list(frequency.values()))
            
            j += 1

        return maxLength