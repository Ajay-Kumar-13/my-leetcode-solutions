import re

class Codec:
    
    def convertToString(self, root, ans):
        
        if root is None:
            return ans
        
        ans += (str(root.val) + '(')
        
        ans = self.convertToString(root.left, ans)
        
        ans += ')('
        
        ans = self.convertToString(root.right, ans)
        
        if ans[-1] == "(":
            ans = ans[:-1]
        else:
            ans += ")"
        
        return ans
        
    def serialize(self, root):
        return self.convertToString(root, "")        

    def deserialize(self, data):
        if not data:
            return None
            
        data = re.findall(r"-\d+|\d+|[()]", data)
        roots = []
        root = None
        
        for element in data:
            if element is not "(" and element is not ")":
                newNode = TreeNode(int(element))
                if not root:
                    root = newNode
                if len(roots) > 0:
                    if roots[-1][0].left is None and not roots[-1][1]:
                        roots[-1][1] = True
                        roots[-1][0].left = newNode
                    else:
                        roots[-1][0].right = newNode
                roots.append([newNode, False])
                
            elif element is ")" and roots[-1][1]:
                roots.pop()
                
            elif element is ")":
                roots[-1][1] = True
                
        return root