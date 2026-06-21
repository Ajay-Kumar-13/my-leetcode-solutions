class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        frequency = {}
        frequency[0] = 1
        total = 0
        ans = 0
        for x in nums:
            total += x
            ans += (frequency.get(total-goal, 0))
            frequency[total] = frequency.get(total, 0) + 1
            

        return ans 