class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mappings = {}
        s = list(s)
        t = list(t)

        i = 0
        for ele in s:
            if ele not in mappings and t[i] not in mappings.values():
                mappings[ele] = t[i]
            
            if ele not in mappings:
                return False
                
            if mappings[ele] != t[i]:
                return False
            i += 1

        return True
        