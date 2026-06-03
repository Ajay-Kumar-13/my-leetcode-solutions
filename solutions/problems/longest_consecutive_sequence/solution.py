class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i = 0
        count = 1
        longest_count = 1

        if(len(nums) == 1 or len(nums) == 0):
            return len(nums)

        for j in range(1, len(nums)):
            diff = nums[j] - nums[i]
            i += 1
            if diff == 1:
                count += 1
                longest_count = max(count, longest_count)
            elif diff > 0:
                count = 1
        return longest_count