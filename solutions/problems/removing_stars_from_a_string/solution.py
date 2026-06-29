class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        stack = []
        
        for x in s:
            if len(stack) > 0 and x == "*" and stack[-1] != "*":
                stack.pop()
                continue
            stack.append(x)
        
        return ''.join(stack)