class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str        :type k: int
        :rtype: int
        """
        
        i = 0
        j = 0
        window = {}
        
        longestSubstringLength = 0
        maxFreq = 0
        
        while j < len(s):
            window[s[j]] = window.get(s[j],0)+1
            maxFreq = max(maxFreq, window.get(s[j]))
            window_length = j - i + 1
            
            while window_length - maxFreq > k:
                window[s[i]] = window.get(s[i],0)-1
                i += 1
                window_length = j - i + 1
                
            longestSubstringLength = max(longestSubstringLength, window_length)
            j += 1
            
        return longestSubstringLength