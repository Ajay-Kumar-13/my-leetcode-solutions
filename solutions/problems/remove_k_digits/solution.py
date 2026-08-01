class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        stack = []

        for n in num:

            while len(stack) > 0 and k > 0 and int(n) < int(stack[-1]):
                stack.pop()
                k -= 1
            
            stack.append(n)

        while k > 0:
            stack.pop()
            k -= 1

        i = 0
        while len(stack) > 0 and i < len(stack) and stack[i] == "0":
            i += 1
        
        if len(stack[i:]) > 0:
            return ''.join(stack[i:])
        
        return "0"