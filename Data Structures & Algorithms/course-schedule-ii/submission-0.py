class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        for src, dst in prerequisites:
            adj[src].append(dst)
        
        topSort = []
        visit = set()
        path = set()
        for i in range(numCourses):
            if not self.dfs(i, adj, visit, path, topSort):
                return []

        # no need to reverse
        return topSort
    
    def dfs(self, src, adj, visit, path, topSort):
        if src in path:
            return False
        if src in visit:
            return True
        path.add(src)
        visit.add(src)

        acyclic = True
        for neighbor in adj[src]:
            acyclic = acyclic and self.dfs(neighbor, adj, visit, path, topSort)
        # postorder
        topSort.append(src)
        path.remove(src)
        return acyclic
        
    