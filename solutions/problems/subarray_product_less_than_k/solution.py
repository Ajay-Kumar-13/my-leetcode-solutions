class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        i = 0
        j = 0

        count = 0

        product = 1

        while j < len(nums):

            product *= nums[j]


            while product >= k and i < j:
                product /= nums[i]
                i += 1
                
            
            if product < k:
                count += j-i+1

            j += 1
            
        return count