class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s) == 0:
            return 0

        i = 0 
        j = i + 1

        window  = {}
        size = 1
        window[s[0]] = 1
        maxSize = 1

        while j < len(s):
            if window.get(s[j], 0) <= 0:
                window[s[j]] = 1
                size += 1
                if size > maxSize:
                    maxSize = size
            else:
                while s[i] != s[j] and i < j:
                    window[s[i]] = window.get(s[i]) - 1
                    i += 1
                window[s[i]] = window.get(s[i]) - 1
                window[s[j]] = window.get(s[j], 0) + 1
                i += 1
                size = j - i + 1
            j += 1

        return maxSize