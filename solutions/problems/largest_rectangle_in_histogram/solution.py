class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        if n == 0:
            return 0
            
        maxArea = 0
        
        
        nse = [len(heights)]*len(heights)
        pse = [-1] * len(heights)
        
        stack = []
        
        for i in range(len(heights)):
            while len(stack) > 0 and heights[stack[-1]] > heights[i]:
                nse[stack[-1]] = i
                stack.pop()
            stack.append(i)
            
        stack =[]
        
        for i in range(len(heights)-1, -1, -1):
            while len(stack) > 0 and heights[stack[-1]] > heights[i]:
                pse[stack[-1]] = i
                stack.pop()
            stack.append(i)
            
        maxArea = 0
        
        for i in range(len(heights)):
            b = (nse[i]-pse[i]-1)
            l = heights[i]
            area = l * b
            maxArea = max(area, maxArea)
            
        return maxArea