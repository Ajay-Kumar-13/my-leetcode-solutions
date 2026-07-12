class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        
        total = 0
        
        sums = {}
        sums[0] = 1

        s = 0

        for element in nums:
            s += element
            val = (s - goal)
            total += sums.get(val, 0)
            sums[s] = sums.get(s, 0)+1

        return total