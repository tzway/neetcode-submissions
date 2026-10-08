# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create one empty node
        newlist = ListNode()
        curr = newlist

        while list1 and list2:
            if list1.val < list2.val:
                temp = list1.next
                list1.next = None
                curr.next = list1
                curr = curr.next
                list1 = temp
            else:
                temp = list2.next
                list2.next = None
                curr.next = list2
                curr = curr.next
                list2 = temp

        if list1:
            curr.next = list1
        if list2:
            curr.next = list2

        return newlist.next


