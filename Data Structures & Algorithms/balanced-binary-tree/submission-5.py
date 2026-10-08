# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return 0, True
            
            leftH, leftB = dfs(root.left)
            rightH, rightB = dfs(root.right)

            rootH = max(leftH, rightH) +1
            rootB = bool(-1<=leftH - rightH<=1 and leftB and rightB)
            return rootH, rootB
        
        return dfs(root)[1]