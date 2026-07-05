class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        if len(s1) > len(s2):
            return False
        
        s1_freq = {}
        
        for element in s1:
            s1_freq[element] = s1_freq.get(element, 0)+1
            
        window = {}
        
        formed = 0
        requirement = len(s1_freq)
        
        i = 0
        while i < len(s1):
            window[s2[i]] = window.get(s2[i], 0)+1
            if window.get(s2[i]) == s1_freq.get(s2[i]) :
                formed += 1
            if formed == requirement:
                return True
            i += 1
        
        
            
        while i < len(s2):
            j = i - len(s1)
            if window.get(s2[j]) >= s1_freq.get(s2[j], 0) and window.get(s2[j]) - 1 < s1_freq.get(s2[j], 0) and formed > 0:
                formed -= 1
            window[s2[j]] = window.get(s2[j]) - 1
            if window.get(s2[j]) == 0:
                del window[s2[j]]
            window[s2[i]] = window.get(s2[i], 0)+1
            if window.get(s2[i]) == s1_freq.get(s2[i]):
                formed += 1
            if formed == requirement:
                return True
            i += 1
            
        return False