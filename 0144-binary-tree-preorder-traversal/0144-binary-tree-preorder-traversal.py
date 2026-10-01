class Solution(object):
    def preorderTraversal(self, root):
        result = []
        
        def traverse(node):
            if not node:
                return
            
            result.append(node.val)  # Root
            traverse(node.left)      # Left
            traverse(node.right)     # Right
            
        traverse(root)
        return result
        