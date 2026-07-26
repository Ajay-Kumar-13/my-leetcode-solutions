class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        n = len(heights)

        nextSmaller = [n-1] * n
        prevSmaller = [0] * n

        stack = []
        for i in range(n):
            while len(stack) > 0 and heights[stack[-1]] > heights[i]:
                nextSmaller[stack[-1]] = i-1
                stack.pop()
            stack.append(i)

        stack = []
        for i in range(n-1, -1, -1):
            while len(stack) > 0 and heights[stack[-1]] > heights[i]:
                prevSmaller[stack[-1]] = i+1
                stack.pop()
            stack.append(i)

        print(nextSmaller)
        print(prevSmaller)


        maxArea = -float('inf')
        for i in range(n):

            l = nextSmaller[i] - prevSmaller[i] + 1

            maxArea = max(maxArea, (l*heights[i]))

        return maxArea        