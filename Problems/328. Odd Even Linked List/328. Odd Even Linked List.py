# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Exclude list of size 1 or 0.
        if not (head and head.next):
            return head;
        
        # Separate the list.
        odd = head;
        even = head.next;
        evenHead = even;
        
        while even and even.next:
            # Connect odd with the next odd.
            odd.next = even.next;
            odd = odd.next;
            
            # Connect even with the next even.
            even.next = odd.next;
            even = even.next;
        
        # Connect the odd list to the even list.
        odd.next = evenHead;
        
        return head;