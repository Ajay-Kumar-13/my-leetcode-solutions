class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        l = len(arr)

        NS = [l]*l
        PS = [-1]*l

        stack = []
        for i in range(l):
            while len(stack) > 0 and arr[stack[-1]] >= arr[i]:
                NS[stack[-1]] = i
                stack.pop()
            stack.append(i)
            
        stack=[]
        for i in range(l-1, -1, -1):
            while len(stack) > 0 and arr[stack[-1]] > arr[i]:
                PS[stack[-1]] = i
                stack.pop()
            stack.append(i)
            
        count = 0
        for i in range(l):
            count += (arr[i]*(NS[i]-i)*(i-PS[i]))

        return count % 1000000007