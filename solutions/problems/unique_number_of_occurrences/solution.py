class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        mappings = {}

        for num in arr:
            count = arr.count(num)
            if num not in mappings:
                if count in mappings.values():
                    return False
                mappings[num] = count

        return True 