"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return head

        pointersNew = []
        pointersOld = []
        

        while head:
            pointersOld.append(head)
            pointersNew.append(Node(head.val))
            head = head.next

        for new, old in zip(pointersNew, pointersOld):
            if old.next:
                new.next = pointersNew[pointersOld.index(old.next)]
            if old.random:
                new.random = pointersNew[pointersOld.index(old.random)]
        return pointersNew[0]

        
        
        