class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        i = 0
        j = i + 1
        k = len(nums) - 1

        nums.sort()

        output = []

        while i < len(nums) - 2:
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == 0:
                    output.append([nums[i], nums[j], nums[k]])

                if s <= 0:
                    while nums[j] == nums[j+1] and j < len(nums) - 2:
                        j += 1
                    j += 1
                elif s >= 0:
                    while nums[k] == nums[k-1] and k > i:
                        k -= 1
                    k -= 1
            
            while nums[i] == nums[i+1] and i < len(nums) -2:
                i += 1
            i += 1
            j = i + 1
            k = len(nums) - 1

        return output