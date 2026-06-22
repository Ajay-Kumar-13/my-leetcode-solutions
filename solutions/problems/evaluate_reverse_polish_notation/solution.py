class Solution:
    def performOperation(self, a, b, operation):
        match operation:
            case "ADD":
                return a + b

            case "SUBTRACT":
                return a - b

            case "MULTIPLY":
                return a * b

            case "DIVISION":
                return int(a/b)

    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            "*": "MULTIPLY",
            "+": "ADD",
            "-": "SUBTRACT",
            "/": "DIVISION"
        }

        stack = []

        i = 0
        top = -1
        
        while i < len(tokens):
            if not operations.get(tokens[i]):
                stack.append(tokens[i])
                top += 1
            else:
                answer = self.performOperation(int(stack[top-1]), int(stack[top]), operations.get(tokens[i]))
                stack.pop()
                top -= 1
                stack[top] = answer
                
            i += 1

        return int(stack[0])