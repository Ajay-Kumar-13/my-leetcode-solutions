class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        nge = {}

        stack = []
        
        ans = []

        for x in nums2:
            nge[x] = nge.get(x, -1)
            while len(stack) > 0 and x > stack[-1]:
                nge[stack[-1]] = x
                stack.pop()
            stack.append(x)
            
        for x in nums1:
            ans.append(nge.get(x))
            
        return ans