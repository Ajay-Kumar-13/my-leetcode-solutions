class Solution(object):
    def removeKdigits(self, nums, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        
        stack = []
        
        elementsSkipped = 0

        if k == len(nums):
            return '0'
        
        for i in range(len(nums)):
            n = nums[i]
            
            while len(stack) > 0 and int(n) < int(stack[-1]) and elementsSkipped < k:
                elementsSkipped += 1
                stack.pop()
            
            stack.append(n)
            
        if elementsSkipped < k:
            for i in range(k-elementsSkipped):
                stack.pop()

        i = 0
        while i < len(stack) and stack[i] == '0':
            i += 1

        ans = ''.join(stack[i:])
        
        # If ans is empty (meaning all characters were zeros), return '0'
        return ans if len(ans) > 0 else '0'
        