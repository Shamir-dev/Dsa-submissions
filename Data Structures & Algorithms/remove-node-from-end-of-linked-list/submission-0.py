# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        first = dummy
        second = dummy 
        #move first ahead by n+1 steps
        for i in range(n+1):
            first = first.next
        #Move both until first hits removeNthFromEnd
        while first:
            first = first.next
            second = second.next
        #Delete Target Nodes BC
        second.next= second.next.next

        return dummy.next
        