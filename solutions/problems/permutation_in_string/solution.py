class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        if len(s1) > len(s2):
            return False

        j = 0
        frequency = {}
        s1Frequency = {}

        for x in s1:
            s1Frequency[x] = s1Frequency.get(x, 0) + 1

        while j < len(s1):
            frequency[s2[j]] = frequency.get(s2[j], 0) + 1
            j += 1

        k = 0
        i = 0

        while j <= len(s2):
            freq = frequency.get(s1[k], 0)
            if freq == s1Frequency.get(s1[k]):
                k += 1
                if k == len(s1):
                    return True
            else:
                if j == len(s2):
                    return False
                k = 0
                frequency[s2[i]] = frequency.get(s2[i], 0) - 1
                i += 1
                frequency[s2[j]] = frequency.get(s2[j], 0) + 1
                j += 1

        return False