# 一条深度遍历访问到两次那么有环
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqMap = defaultdict(list)
        for course, prereq in prerequisites:
            prereqMap[course].append(prereq)
        print(prereqMap)
        
        hasLoop = False

        def dfs(course, visit):
            nonlocal hasLoop
            # loop detected
            if course in visit:
                hasLoop = True
                return
            
            

            for prereq in prereqMap[course]:
                visit.add(course)
                dfs(prereq, visit)
                visit.remove(course)

            return 

        for course in list(prereqMap):
            dfs(course, set())
            if hasLoop: return False
        
        return True
