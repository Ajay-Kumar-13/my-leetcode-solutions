class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        if len(p) > len(s):
            return []

        p_dict = {}

        for element in p:
            p_dict[element] = p_dict.get(element, 0)+1

        requirement = len(p_dict)

        window = {}

        formed = 0

        ans = []

        for _ in range(len(p)):
            val = s[_]
            window[val] = window.get(val, 0)+1
            if p_dict.get(val) == window.get(val):
                formed += 1
            if formed == requirement:
                ans.append(0)

        i = 1
        j = len(p)

        while j < len(s):
            if window.get(s[i-1], 0) == p_dict.get(s[i-1], 0) and window.get(s[i-1], 0) - 1 < p_dict.get(s[i-1], 0) and formed > 0:
                formed -= 1

            window[s[i-1]] = window.get(s[i-1], 0) - 1
            if window.get(s[i-1], 0) == 0:
                del window[s[i-1]]
            window[s[j]] = window.get(s[j], 0) + 1

            if window.get(s[j], 0) == p_dict.get(s[j], 0):
                formed += 1
            if formed == requirement:
                ans.append(i) 
            j += 1
            i += 1

        return ans