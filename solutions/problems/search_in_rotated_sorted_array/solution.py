class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        i = 0
        j = len(nums) - 1

        while i <= j:
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            if nums[i] < nums[mid] and nums[i] <= target and target <= nums[mid]:
                j = mid - 1
            elif nums[i] < nums[mid]:
                i = mid + 1
            elif nums[mid] < nums[j] and nums[mid] <= target and target <= nums[j]:
                i = mid + 1
            elif nums[mid] < nums[j]:
                j = mid - 1
            else:
                i = mid+1
            
        return -1