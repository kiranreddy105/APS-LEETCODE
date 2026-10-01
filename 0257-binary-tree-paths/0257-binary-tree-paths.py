class Solution(object):
    def binaryTreePaths(self, root):
        result = []
        
        def dfs(node, path):
            if not node.left and not node.right:
                result.append(path + str(node.val))
            
            if node.left:
                dfs(node.left, path + str(node.val) + "->")
            
            if node.right:
                dfs(node.right, path + str(node.val) + "->")
                
        if root:
            dfs(root, "")
            
        return result
        
        