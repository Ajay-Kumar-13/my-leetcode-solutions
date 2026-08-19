class Solution:
    def maxPathSum(self, root):

        def getMaxPath(root, ans):

            if root is None:
                return -float('inf'), ans

            L, ans = getMaxPath(root.left, ans)
            
            R, ans = getMaxPath(root.right, ans)
            
            value = max(L+root.val, R+root.val, root.val)
            
            ans = max(value, ans, L+R+root.val)
            
            return value, ans
        
        return getMaxPath(root, -float('inf'))[1]
        