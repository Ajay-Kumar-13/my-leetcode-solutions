class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = len(nums) / 2
        mappings = {}

        for num in nums:
            if num not in mappings:
                mappings[num] = 1
            else:
                mappings[num] += 1

            if mappings.get(num) > k:
                return num