class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        window = {}

        i = 0
        j = 0
        max_sum = 0
        s = 0

        while j < len(nums):
            window[nums[j]] = window.get(nums[j], 0)+1

            if window.get(nums[j]) > 1:
                while window.get(nums[j]) > 1 and i < j:
                    s -= nums[i]
                    window[nums[i]] = window.get(nums[i], 0)-1
                    if window.get(nums[i]) == 0:
                        del window[nums[i]]
                    i += 1

            s += nums[j]

            if len(window) == k:
                if s > max_sum:
                    max_sum = s
                s -= nums[i]
                window[nums[i]] = window.get(nums[i]) - 1
                if window.get(nums[i]) == 0:
                    del window[nums[i]]
                i += 1
            
            j += 1

        return max_sum
        