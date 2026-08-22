class Solution(object):
    def removeDuplicates(self, s, k):

        stack = []

        for element in s:
            
            if len(stack) > 0 and stack[-1][0] == element:
                stack.append((element, stack[-1][1]+1))
            else:
                stack.append((element, 1))
            
            if len(stack) > 0 and stack[-1][1] == k:
                while len(stack) > 0 and stack[-1][0] == element:
                    stack.pop()

        return "".join(map(lambda x: x[0], stack))