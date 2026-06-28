class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()

        ans = set()

        for i in range(len(nums)-2):
            k = nums[i]
            left = i+1
            right = len(nums)-1

            while left < right:

                s = nums[left] + nums[right]

                if s == -(k):
                    ans.add((nums[left], nums[right], k))
                    left += 1
                    right -= 1
                elif s < -(k):
                    left += 1
                else:
                    right -= 1

        return list(ans)
        