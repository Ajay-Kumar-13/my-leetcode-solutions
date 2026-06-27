class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        frequency = {}
        
        stack = []
        
          
        for x in s:
            
            if len(stack) > 0 and stack[-1] == x:
                stack.pop()
                frequency[x] = frequency.get(x, 0)-1
                continue

            stack.append(x)
            frequency[x] = frequency.get(x, 0)+1

        return ''.join(stack)