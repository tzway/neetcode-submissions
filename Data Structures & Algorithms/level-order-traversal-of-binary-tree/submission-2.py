# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = defaultdict(list)
        res = []
        def dfs(root, depth):

            if not root:
                return

            levels[depth].append(root.val)
            dfs(root.left, depth+1)
            dfs(root.right, depth+1)
            return
        dfs(root, 0)
        for i in range(len(levels)):
            res.append(levels[i])

        return res

