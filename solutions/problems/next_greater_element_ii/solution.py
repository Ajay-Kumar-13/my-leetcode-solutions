class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nge = {}

        stack = []
        
        ans = []

        for j in range(2):
            for i in range(len(nums)):
                nge[i] = nge.get(i, -1)
                while len(stack) > 0 and nums[i] > nums[stack[-1]]:
                    nge[stack[-1]] = i
                    stack.pop()
                stack.append(i)
            
        for i in range(len(nums)):
            index = nge.get(i)
            if index != -1:
                ans.append(nums[index])
            else:
                ans.append(index)
                
        return ans