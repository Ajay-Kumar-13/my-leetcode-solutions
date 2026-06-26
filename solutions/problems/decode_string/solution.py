class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        s = list(s)
        
        decodedString = ""
        
        frequency = {}
        
        stack = []
        
        for i in range(len(s)):
            x = s[i]
            if x == ']':
                
                string = ""
                
                element = stack.pop()
                
                while element != '[':
                    string = element + string
                    element = stack.pop() 
                    
                frequency[element] = frequency.get(element, 0)-1
                    
                k = stack.pop()
                while len(stack) > 0 and stack[-1].isdigit():
                    k = stack.pop() + k
                k = int(k)
                
                if frequency.get('[') <= 0:
                    a = ''.join(stack)
                    stack.clear()
                    decodedString += a
                    decodedString += k*string
                else:
                    stack.append(k*string)
                    
                continue
                                
            stack.append(x)
            
            frequency[x] = frequency.get(x, 0)+1
            
        return decodedString + ''.join(stack)