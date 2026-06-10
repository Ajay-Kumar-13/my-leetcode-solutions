class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        output = []

        for element in nums:
            if element != val:
                output.append(element)

        for i in range(len(output)):
            nums[i] = output[i]
             
        return len(output)
        