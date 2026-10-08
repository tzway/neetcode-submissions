# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1, cur2 = l1, l2
        
        head = cur = ListNode(0)
        carry = 0
        
        while cur1 or cur2:
            if cur1 and cur2:
                sumval = cur1.val + cur2.val + carry
            elif cur1:
                sumval = cur1.val + carry
            elif cur2:
                sumval = cur2.val + carry
            
            if sumval < 10:
                carry = 0
            else:
                carry = 1
            cur.next = ListNode(sumval%10)
            
            cur= cur.next

            if cur1:
                cur1 = cur1.next
            if cur2:
                cur2 = cur2.next
        
        if carry ==1:
            cur.next = ListNode(1)
        return head.next
            