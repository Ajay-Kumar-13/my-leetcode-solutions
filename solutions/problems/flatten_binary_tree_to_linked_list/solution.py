class Solution:
    def flatten(self, root):
        
        if root is None:
            return
        
        self.flatten(root.left)
        
        right = root.right
        
        root.right = root.left
        
        root.left = None
        
        temp = root
        while temp and temp.right:
            temp = temp.right
        
        temp.right = right
        
        self.flatten(root.right)