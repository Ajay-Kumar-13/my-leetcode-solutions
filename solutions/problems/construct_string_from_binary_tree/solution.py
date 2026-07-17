# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getPreOrderString(self, root, ans):
        if not root:
            return ans
        
        if root.left is None and root.right is None:
            ans += str(root.val)
            return ans

        ans += str(root.val)+"("

        ans = self.getPreOrderString(root.left, ans)

        ans += ")("

        ans = self.getPreOrderString(root.right, ans)

        if ans[-1] != "(":
            ans += ")"
        else:
            ans = ans[:len(ans)-1]

        return ans

    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        return self.getPreOrderString(root, "")