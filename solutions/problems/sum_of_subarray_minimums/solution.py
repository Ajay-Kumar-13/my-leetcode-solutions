class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        nse = [0]*len(arr)
        pse = [0]*len(arr)
        
        ans = 0
        
        stack = []
        for i in range(len(arr)):
            while len(stack) > 0 and arr[stack[-1]] >= arr[i]:
                nse[stack[-1]] = i - stack[-1] - 1
                stack.pop()
            stack.append(i)
            
        for ind in stack:
            nse[ind] = len(arr)-1 -ind
            
        stack = []
        for i in range(len(arr)-1, -1, -1):
            while len(stack) > 0 and arr[stack[-1]] > arr[i]:
                pse[stack[-1]] = stack[-1] - i - 1
                stack.pop()
            stack.append(i)
            
        for ind in stack:
            pse[ind] = ind - 0
            
        for i in range(len(arr)):
            ans += ((pse[i]+1) * (nse[i]+1))*arr[i]
            
        MOD = 10**9 + 7
        return ans % MOD
            
        return ans