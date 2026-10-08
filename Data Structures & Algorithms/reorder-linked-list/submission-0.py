# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reorder(head):
            if not head.next:
                return head
            if not head.next.next:
                return head

            rest = head.next
            curr = head

            while curr.next:
                prev = curr
                curr = curr.next

            prev.next = None
            head.next = curr
            curr.next = reorder(rest)

            return head
        reorder(head)