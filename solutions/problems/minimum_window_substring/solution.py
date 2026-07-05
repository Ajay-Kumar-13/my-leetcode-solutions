class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        tfreq = {}
        for element in t:
            tfreq[element] = tfreq.get(element, 0) + 1
        
        requirement = len(tfreq)
        formed = 0
        sfreq = {}
        ans = ""
        i = 0
        minString = s
        
        for j in range(len(s)):
            
            sfreq[s[j]] = sfreq.get(s[j], 0)+1
            if sfreq.get(s[j]) == tfreq.get(s[j]):
                formed += 1
                
            while formed == requirement and i <= j:
                if len(s[i:j+1]) <= len(minString):
                    minString = s[i:j+1]
                    ans = minString
                if sfreq.get(s[i]) >= tfreq.get(s[i], 0) and sfreq.get(s[i]) - 1 < tfreq.get(s[i], 0) and formed > 0:
                    formed -= 1
                sfreq[s[i]] = sfreq.get(s[i])-1
                i += 1
                
        return ans