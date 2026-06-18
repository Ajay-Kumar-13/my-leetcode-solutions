class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        frequency = {}
        maxi = 0
        vowels = ['a', 'e', 'i', 'o', 'u']
        for x in range(k):
            frequency[s[x]] = frequency.get(s[x],0)+1
            if s[x] in vowels:
                maxi += 1

        i = 0
        count = maxi
        for x in range(k, len(s)):
            i += 1
            if s[i-1] in vowels:
                count -= 1
            if s[x] in vowels:
                count += 1
            
            maxi = max(count, maxi)

        return maxi