class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        mappings = {}

        for i in range(len(numbers)):
            d = target - numbers[i]
            if d not in mappings:
                mappings[numbers[i]] = i
            else:
                return [mappings.get(d)+1, i+1]