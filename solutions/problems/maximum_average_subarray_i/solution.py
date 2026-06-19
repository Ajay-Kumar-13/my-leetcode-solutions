class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        maxi = -float('inf')
        sum = 0
        for i in range(k):
            sum += nums[i]

        maxi = max(maxi, float(sum)/k)

        i = 0
        for j in range(k, len(nums)):
            sum += nums[j]
            sum -= nums[i]
            i += 1
            maxi = max(maxi, float(sum)/k)

        return maxi