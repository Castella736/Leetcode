# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Find mid point using f-s two pointers.
        p1 = p2 = head;
        while p2.next and p2.next.next:
            p1 = p1.next;
            p2 = p2.next.next;
        
        # Reverse the later half list.
        p2 = p1.next;
        p1.next = None;
        prev = None
        while p2 is not None:
            p2.next, p2, prev = prev, p2.next, p2;
            
        # Concatenate two lists alternatively.
        p1 = head;
        p2 = prev; # At this stage, prev is the tail of the list.
        while p2 is not None:
            p1.next, p1 = p2, p1.next;
            p2.next, p2 = p1, p2.next;
        
        return None;