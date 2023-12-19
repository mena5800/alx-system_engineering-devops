class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        path1 = []
        path2 = []
        path = []
        
        def dfs(node, path):
            
            if node == None:
                return
            
            path.append(node.val)
            
            if path[-1] == q.val:
                path1 = [val for val in path]
                print(path1)
            if path[-1] == p.val:
                path2 = [val for val in path]
                print(path2)
            
            left = [val for val in path]
            right = [val for val in path]
            
            dfs(node.left, left)
            dfs(node.right, right)
        
        
        dfs(root, path)
        
        print(path, path1, path2)


root = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))),TreeNode(1, TreeNode(0), TreeNode(8)))
        
q = TreeNode(5)
p = TreeNode(4)

Solution().lowestCommonAncestor(root,q, p)
            
            
        