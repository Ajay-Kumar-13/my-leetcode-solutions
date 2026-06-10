class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        output = [nums[0]]

        for i in range(len(nums)):
            if output[len(output)-1] != nums[i]:
                output.append(nums[i])

        for i in range(len(output)):
            nums[i] = output[i]

        return len(output)