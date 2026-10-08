# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        res = []

        def dfs(root, p, q):
            nonlocal res

            if not root:
                isAncP = isAncQ = False
                return False, False
            
            isAncPleft, isAncQleft = dfs(root.left, p, q)
            isAncPright, isAncQright = dfs(root.right, p, q)
            isAncP = root.val == p.val or isAncPleft or isAncPright
            isAncQ = root.val == q.val or isAncQleft or isAncQright

            if isAncP and isAncQ:
                res.append(root)

            print(f'address: {id(root)}, Val: {root.val}, Anc of P {isAncP}, Anc of Q {isAncQ}')

            return isAncP, isAncQ
        
        dfs(root, p, q)
        return res[0]
    
