# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balance = True
        def depth(root):
            nonlocal balance
            if not root:
                return 0

            dl = depth(root.left)
            dr = depth(root.right)
            print(dl, dr)
            
            if abs(dl - dr) >1:
                balance = False

            return max(dl, dr) +1
        
        depth(root)
        return balance
        