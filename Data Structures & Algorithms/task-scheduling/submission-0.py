from collections import Counter, deque
from heapq import *
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = Counter(tasks)
        maxheap = []
        q= deque()
        for task, count in cnt.items():
            heappush(maxheap, (-count, task))
        print(maxheap)
        print(q)
        
        time = 0
        while maxheap or q:
            time +=1
            if q and time == q[0][0]:
                _, c, t = q.popleft()
                heappush(maxheap, (c,t))
            if maxheap:
                c, t = heappop(maxheap)
                if c < -1:
                    q.append((time+n+1,c+1,t))
            
        
        return time
            