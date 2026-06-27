class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        frequency = {}
        
        stack = []
        
        stackFreq = {}
        
        
        for element in s:
            frequency[element] = frequency.get(element, 0) + 1
        
        for element in s:

            frequency[element] = frequency.get(element, 0) - 1

            if stackFreq.get(element) > 0:
                continue
            
            while len(stack) > 0 and stack[-1] > element and frequency.get(stack[-1]) >= 1:
                stackFreq[stack[-1]] = stackFreq.get(stack[-1], 0) - 1
                stack.pop()
                
            if stackFreq.get(element, 0) <= 0:
                stack.append(element)
                stackFreq[element] = stackFreq.get(element, 0) + 1
            
            
            
        
        return ''.join(stack)