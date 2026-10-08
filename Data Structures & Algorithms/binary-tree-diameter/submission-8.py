# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.maxDi = 0  # Instance variable to hold the maximum diameter

    def depth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # Recursively find the depth of left and right subtrees
        depL = self.depth(root.left)
        depR = self.depth(root.right)

        # Calculate the current depth
        dep = max(depL, depR) + 1

        # Update the maximum diameter (which is the sum of left and right depths)
        self.maxDi = max(self.maxDi, depL + depR)

        return dep

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDi = 0  # Initialize maxDi to 0
        self.depth(root)  # Start the depth-first search

        return self.maxDi  # Return the computed maximum diameter
