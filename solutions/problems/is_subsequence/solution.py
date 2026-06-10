class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        s = list(s)

        t = list(t)

        i = 0

        if len(s) == 0:
            return True

        for element in t:
            if i < len(s) and element == s[i]:
                i += 1
            
        if i >= len(s):
            return True
        else:
            return False