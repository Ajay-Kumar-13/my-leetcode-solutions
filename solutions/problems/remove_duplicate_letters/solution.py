class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
    
        frequency = {}

        for ele in s:
            frequency[ele] = frequency.get(ele, 0)+1 

        stack = []
        

        for ele in s:
            
            if ele not in stack:
                while len(stack) > 0 and frequency.get(stack[-1]) > 0 and stack[-1] > ele:
                    top = stack.pop()

                stack.append(ele)
                
            frequency[ele] = frequency.get(ele) - 1

        if stack:
            return "".join(stack)

        return ''