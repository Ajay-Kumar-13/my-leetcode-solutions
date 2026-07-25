class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        nextGreater = [0]*len(temperatures)

        stack = []

        for i, temp in enumerate(temperatures):
            while len(stack) > 0 and temp > stack[-1][0]:
                nextGreater[stack[-1][1]] = i - stack[-1][1] 
                stack.pop()
            
            stack.append((temp, i))

        return nextGreater