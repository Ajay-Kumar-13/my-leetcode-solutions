class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        i = 0
        j = i+1
        k = j+1
        e = len(nums) - 1

        output = []

        nums.sort()

        while i < len(nums) - 3:
            while j < k and j < len(nums) - 2:
                while k < e:
                    s = nums[i] + nums[j] + nums[k] + nums[e]
                    if s == target:
                        output.append([nums[i], nums[j], nums[k], nums[e]])
                    
                    if s <= target:
                        while nums[k] == nums[k+1] and k < e-1:
                            k += 1
                        k += 1
                    
                    if s >= target:
                        while nums[e] == nums[e-1] and e > k:
                            e -= 1
                        e -= 1
                
                while nums[j] == nums[j+1] and j < len(nums) - 2:
                    j += 1
                j += 1
                k = j + 1
                e = len(nums) - 1
                
            while nums[i] == nums[i+1] and i < len(nums) - 3:
                i += 1
            i += 1
            j = i+1
            k = j+1
            e = len(nums) - 1

        return output