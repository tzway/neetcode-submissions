# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
maxDi = 0
def depth(root):
    global maxDi
    if not root:
        return 0
    depL = depth(root.left)
    depR = depth(root.right)
    dep = max(depL,depR) + 1
    print(depL, depR, dep)
    
    maxDi = max(maxDi, depL+depR)
    print(maxDi)
    
    return dep
class Solution:


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        global maxDi
        maxDi = 0

        depth(root)
        
        return maxDi
        