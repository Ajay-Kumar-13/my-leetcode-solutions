class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        s= list(s)
        first_odd_taken = False
        mappings = {}
        count = 0

        for char in s:
            if char not in mappings:
                total = s.count(char)
                mappings[char] = total
                if (total%2 != 0) and not first_odd_taken:
                    count += total
                    first_odd_taken = True
                elif (total%2 != 0):
                    count += (total - 1)
                else:
                    count += total
        return count