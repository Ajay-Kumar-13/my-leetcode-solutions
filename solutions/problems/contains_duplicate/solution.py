class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        setOfNums = set(nums)
        if len(nums) == len(setOfNums):
            return False
        else:
            return True