class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        closestDiff = 100000
        closestSum = 0
        i = 0
        j = i + 1
        k = len(nums) -1 

        nums.sort()

        while i < len(nums) - 2:
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s < target:
                    if min(target-s, closestDiff) < closestDiff:
                        closestSum = s
                    closestDiff = min(target-s, closestDiff)
                else:
                    if min(s-target, closestDiff) < closestDiff:
                        closestSum = s
                    closestDiff = min(s-target, closestDiff)

                if s == target:
                    return closestSum

                if s < target:
                    while nums[j] == nums[j+1] and j < len(nums)-2:
                        j += 1
                    j += 1
                elif s > target:
                    while nums[k] == nums[k-1] and k > i:
                        k -= 1
                    k -= 1
            while nums[i] == nums[i+1] and i < len(nums) - 2:
                i += 1
            i += 1
            j = i+1
            k = len(nums) - 1

        return closestSum