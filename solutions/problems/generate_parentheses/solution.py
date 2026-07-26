class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def validParenthesis(parenthesis):
            stack = []

            for element in parenthesis:
                if len(stack) > 0 and stack[-1] == "(" and element is ")":
                    stack.pop()
                else:
                    stack.append(element)

            if len(stack) == 0:
                return True

            return False

        answer = set([])

        def generateCombinations(n, parenthesis):

            if len(parenthesis) == n*2:
                print(''.join(parenthesis))
                if validParenthesis(parenthesis):
                    answer.add(''.join(parenthesis))
                return

            parenthesis.append("(")
            generateCombinations(n, parenthesis) 

            parenthesis.pop()
            parenthesis.append(")")
            generateCombinations(n, parenthesis) 

            parenthesis.pop()

            return 

        
        generateCombinations(n, [])
        return list(answer)