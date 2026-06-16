class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        frequency = {}
        frequency[0] = 1
        total = 0
        ans = 0
        for x in nums:
            total += x
            ans += (frequency.get(total-k, 0))
            frequency[total] = frequency.get(total, 0) + 1
            

        return ans 