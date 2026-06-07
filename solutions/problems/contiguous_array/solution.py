class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mappings = {}
        s = 0
        count = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                s += -1
            else:
                s += 1

            if s in mappings:
                count = max(count, i - mappings.get(s))
            else:
                mappings[s] = i

            if s == 0:
                count = max(count, i+1)
            


        return count