class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        Anagrams = {}
        for word in strs:
            key = "".join(sorted(word))
            if key not in Anagrams:
                Anagrams[key] = []
            Anagrams[key].append(word)

        return Anagrams.values()