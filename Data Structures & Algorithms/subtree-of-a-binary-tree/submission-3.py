# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(p, q):
            if p == q == None:
                return True
            
            if bool(p) != bool(q):
                return False
            
            if p.val != q.val:
                return False

            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        res = False

        def dfs(root):
            nonlocal res
            if res == True:
                return

            if isSameTree(root, subRoot):
                res = True

            if not root:
                return
            
            dfs(root.left)
            dfs(root.right)
            return

        dfs(root)

        return res
