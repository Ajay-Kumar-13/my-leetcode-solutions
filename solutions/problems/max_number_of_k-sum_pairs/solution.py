class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        i = 0
        j = len(nums) - 1

        nums.sort()
        
        count = 0

        while i < j:
            s = nums[i] + nums[j]

            if s == k:
                count += 1
                i += 1
                j -= 1
            
            elif s < k:
                i += 1

            elif s > k:
                j -= 1

        return count