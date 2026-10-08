# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(root,arr):
            if not root:
                arr.append(None)
                return
            
            dfs(root.left,arr)
            dfs(root.right,arr)
            arr.append(root.val)
            return
        arr = []
        arrSub = []
        dfs(root,arr)
        dfs(subRoot, arrSub)

        def is_sublist(sublist, main_list):
            # Convert both lists to strings to check for the presence of the sublist
            sublist_str = ','.join(map(str, sublist))
            main_list_str = ','.join(map(str, main_list))
            
            return sublist_str in main_list_str

            
        print(arr)
        print(arrSub)

        return is_sublist(arrSub, arr)
        