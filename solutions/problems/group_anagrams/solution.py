class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        mappings = {}

        for element in strs:
            sortedEle = ''.join(sorted(element))
            if sortedEle in mappings:
                anagrams = mappings.get(sortedEle)
                anagrams.append(element)
            else:
                mappings[sortedEle] = [element]

        return list(mappings.values())