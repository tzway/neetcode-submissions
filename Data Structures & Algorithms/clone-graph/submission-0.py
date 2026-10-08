"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        
        if not node.neighbors:
            return Node(node.val)

        adjMap = defaultdict(list)

        def dfs(node):
            if node.val in adjMap:
                return
            
            for neighbor in node.neighbors:
                adjMap[node.val].append(neighbor.val)
                dfs(neighbor)
        
        dfs(node)
        print(adjMap)

        valNodeMap = {}
        for val in adjMap:
            valNodeMap[val] = Node(val,None)
        
        print(valNodeMap)

        for val, neiVals in adjMap.items():
            valNodeMap[val].neighbors = [valNodeMap[nv] for nv in neiVals]

        return valNodeMap[1]

        