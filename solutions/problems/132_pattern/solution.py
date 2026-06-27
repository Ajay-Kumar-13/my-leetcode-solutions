class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stack = []

        medium_right = -float('inf')

        for i in range(len(nums)-1,-1,-1):
            val = nums[i]

            while len(stack) > 0 and stack[-1] < val:
                medium_right = max(medium_right, stack[-1])
                stack.pop()

            if val < medium_right:
                return True

            stack.append(val)
        
        return False
        