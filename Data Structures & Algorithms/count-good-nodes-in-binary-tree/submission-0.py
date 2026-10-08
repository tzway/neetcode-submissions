# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(root, maxV):
            nonlocal res
            if not root:
                return 
            if root.val >= maxV:
                res += 1
                maxV = root.val
            dfs(root.left, maxV)
            dfs(root.right, maxV)
        
        dfs(root, -999)
        return res
                