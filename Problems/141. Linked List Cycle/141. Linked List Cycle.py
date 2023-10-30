# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p1, p2 = head, head;
        
        # Execute until reaching the end.
        while p2 and p2.next:
            p1 = p1.next;
            p2 = p2.next.next;
        
            # Check if two pointers meet.
            if p1==p2:
                return True;
            
        # The while-loop ends if p2 reach the end.
        # That is, no loop.
        return False;