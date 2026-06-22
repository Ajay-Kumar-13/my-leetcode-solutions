class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        paranthesis = list(s)
        if len(paranthesis) < 2:
            return False
            
        stack = []
        top = -1
        
        keys = {
            "(":")",
            "[":"]",
            "{":"}"
        }
        
        i = 0
        
        while i < len(paranthesis):
            if keys.get(paranthesis[i]):
                stack.append(paranthesis[i])
                top += 1
            elif top >= 0 and keys.get(stack[top]) == paranthesis[i]:
                stack.pop()
                top -= 1
            else:
                return False
            i += 1
        
        if top != -1:
            return False

        return True