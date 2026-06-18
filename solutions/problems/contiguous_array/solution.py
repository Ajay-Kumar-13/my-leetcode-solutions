class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        frequency = {}
        sums = {}
        total = 0
        maxLength = 0
        for i,x in enumerate(nums):
            frequency[x] = frequency.get(x, 0)+1
            if x == 0:
                x = -1
            total += x
            if total not in sums:
                sums[total] = i
            else:
                maxLength = max(maxLength, i-sums.get(total))

            if total == 0:
                maxLength = max(maxLength, i+1)

        return maxLength