class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']

        s = list(s)

        i = 0
        j = len(s)-1

        while i < j:
            while s[i] not in vowels and i < j:
                i += 1
            
            while s[j] not in vowels and i < j:
                j -= 1

            if i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        return "".join(s)
            