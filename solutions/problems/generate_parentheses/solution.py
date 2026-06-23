class Solution:
    
    def __init__(self):
        self.ans = []
        self.frequency = {}
        
    def isValid(self, paranthesis):

        if len(paranthesis) < 2:
            return False
            
        stack = []
        top = -1
        
        keys = {
            "(":")",
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
    
    def backtrack(self, n, parantheses):
        
        # Base case
        if len(parantheses) == n*2:
            if self.isValid(parantheses):
                self.ans.append(''.join(parantheses))
            return
        
        # Decision 1: Include (
        count = self.frequency.get('(', 0)
        if count < n:
            parantheses.append('(')
            self.frequency['('] = self.frequency.get('(', 0)+1
            self.backtrack(n, parantheses)
            ele = parantheses.pop()
            self.frequency[ele] = self.frequency.get(ele) - 1
            
        
        # Decision 2: Include )
        count = self.frequency.get(')', 0)
        if count < n:
            parantheses.append(')')
            self.frequency[')'] = self.frequency.get(')', 0)+1
            self.backtrack(n, parantheses)
            ele = parantheses.pop()
            self.frequency[ele] = self.frequency.get(ele) - 1
            
        return
    
    def generateParenthesis(self, n):
        self.backtrack(n, [])
        return self.ans