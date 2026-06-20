class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(p) > len(s):
            return []

        window_length = len(p)

        requirement = {}
        window = {}
        
        s = list(s)

        for x in p:
            requirement[x] = requirement.get(x, 0) + 1

        ans = []

        formed = 0

        for i in range(len(p)):
            window[s[i]] = window.get(s[i], 0)+1
            if window.get(s[i]) == requirement.get(s[i]):
                formed += 1
            if formed == len(requirement):
                ans.append(0)

        i = 1
        j = len(p)

        while j < len(s):
            if requirement.get(s[i-1], 0) == window.get(s[i-1], 0):
                formed -= 1
            window[s[i-1]] = window.get(s[i-1]) - 1
            
            window[s[j]] = window.get(s[j], 0) + 1
            if window.get(s[j]) == requirement.get(s[j]):
                formed += 1
            if formed == len(requirement):
                ans.append(i)
            j += 1
            i += 1
            
        return ans