class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        mappings = {}
        
        pattern = list(pattern)
        s = s.split(" ")

        if len(pattern) != len(s):
            return False

        i = 0
        for letter in pattern:
            if letter not in mappings and s[i] not in mappings.values():
                mappings[letter] = s[i]
            
            if mappings.get(letter) != s[i]:
                return False

            i += 1

        return True