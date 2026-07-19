# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import re 

class Codec:

    def getTreeInFormOfString(self, root, ans):
        if not root:
            return ans

        if root.left is None and root.right is None:
            ans += str(root.val)
            return ans

        ans += str(root.val) + '('

        ans = self.getTreeInFormOfString(root.left, ans)
        
        ans += ")("

        ans = self.getTreeInFormOfString(root.right, ans)
        
        if ans[-1] == "(":
            ans = ans[:len(ans)-1]
        else:
            ans += ')'


        return ans
        

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        strFormat = self.getTreeInFormOfString(root, "")
        
        print(strFormat, "after serialization")

        return strFormat


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        def isInteger(s):
            # Strip whitespace and check if the remaining string is an int
            s = s.strip()
            if not s:
                return False
            if s[0] in ('-', '+'):
                return s[1:].isdigit()

            return s.isdigit()

        data = re.findall(r"-\d+|\d+|[()]", data)

        if not data:
            return None

        # stack: top element will be the current node
        currentNode = []

        for i, element in enumerate(data):
            if element is ")" and data[i-1] != "(":
                currentNode.pop()
            elif isInteger(element):
                node = TreeNode(int(element))
                if len(currentNode) > 0:
                    root = currentNode[-1]
                    if not root.left and data[i-2] == str(root.val):
                        root.left = node
                    else:
                        root.right = node

                    currentNode.append(node)
                else:
                    currentNode.append(node) 

        return currentNode[0]