class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def atMost(k):

            frequency = {}
            j = 0
            i = 0
            total = 0
            
            while j < len(nums):
                
                frequency[nums[j]] = frequency.get(nums[j], 0) + 1

                while len(frequency) > k:
                    frequency[nums[i]] = frequency.get(nums[i], 0) - 1
                    if frequency.get(nums[i]) == 0:
                        del frequency[nums[i]]
                    i += 1

                total += (j - i + 1)
                
                j += 1
                
            return total
            
        return atMost(k) - atMost(k-1)