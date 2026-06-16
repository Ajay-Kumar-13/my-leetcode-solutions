class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        start = 0
        end = 0

        frequency = {}
        for x in t:
            frequency[x] = frequency.get(x, 0) + 1

        requirement = len(frequency)
        m = len(s)
        n = len(t)

        i = 0

        while s[i] not in frequency and i < m-1:
            i += 1
            
        j = i

        diff = float('inf')

        window = {}
        formed = 0

        while i <= j:
            while formed < requirement and j < m:
                char = s[j]
                window[char] = window.get(char, 0) + 1
                if char in frequency and window.get(char) == frequency.get(char):
                    formed += 1
                j += 1
            if formed == requirement and diff > (j+1-i):
                diff = j+1-i
                start = i
                end = j
            
            if i < m:
                window[s[i]] = window.get(s[i]) - 1
                if window.get(s[i]) < frequency.get(s[i]):
                    formed -= 1
            
            i += 1
            while i < m - 1 and s[i] not in frequency:
                i += 1
    

        return s[start:end]