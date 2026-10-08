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
        pointers = {} #ListNode:ListNode
        
        curr = head
        while curr:
            pointers[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            if curr.next:
                pointers[curr].next = pointers[curr.next]
            if curr.random:
                pointers[curr].random = pointers[curr.random]

            curr = curr.next
        
        if head:
            return pointers[head]
        return None


        
        
        