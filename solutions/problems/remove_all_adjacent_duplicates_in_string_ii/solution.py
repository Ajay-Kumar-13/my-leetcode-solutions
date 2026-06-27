class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :rtype: str
        """
        
        stack = []
        
        for x in s:
            
            if len(stack) == 0:
                stack.append([x, 1])
                continue
            
            if stack[-1][0] == x and stack[-1][1] == k-1:
                stack.pop()
                continue

            if stack[-1][0] == x:
                stack[-1][1] += 1
            else:
                stack.append([x, 1])
        
        ans = ""
        for t in stack:
            ans += t[0]*t[1]
            
        return ans