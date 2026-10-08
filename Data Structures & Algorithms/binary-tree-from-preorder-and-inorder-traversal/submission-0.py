# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        rootVal = preorder[0]
        i = inorder.index(rootVal)
        inLeft, inRight = inorder[:i], inorder[i+1:]
        preLeft = [val for val in preorder if val in inLeft]
        preRight = [val for val in preorder if val in inRight]
        return TreeNode(rootVal, self.buildTree(preLeft, inLeft), self.buildTree(preRight, inRight))
