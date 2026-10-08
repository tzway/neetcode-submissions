# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        postOrder = []
        def dfs(root):
            if root is None:
                postOrder.append("None")
                return
            
            dfs(root.left)
            dfs(root.right)
            postOrder.append(str(root.val))
        dfs(root)
        return ",".join(postOrder)
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        postOrder = data.split(",")
        for i, v in enumerate(postOrder):
            if v == "None":
                postOrder[i] = None
            else:
                postOrder[i] = int(v)

        stack = []

        for v in postOrder:
            if v is None:
                stack.append(v)
                continue
            right = stack.pop()
            left = stack.pop()
            node = TreeNode(v, left, right)
            stack.append(node)
        print(stack)
        return stack.pop()
