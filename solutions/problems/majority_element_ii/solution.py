class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        k = len(nums) / 3
        mappings = {}
        elements = []

        for num in nums:
            if num not in mappings:
                mappings[num] = 1
            else:
                mappings[num] += 1

        for num,count in mappings.items():
            if count > k:
                elements.append(num)

        return elements
                