# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # middle index = n//2 where n = length of the list.
        # Exclude singleton list.
        if not head.next:
            return None;
        
        # Fast-slow pointers.
        fast, slow = head.next, head;
        
        while fast.next and fast.next.next:
            slow = slow.next;
            fast = fast.next.next;
            
        # Index of fast = 1+2k < n-1.
        # Index of slow = k.
        # If n even, fast.next==None, so n=2+2k.
        # If n odd, fast.next!=None, so n=3+2k.
        # No matter which, the middle index = n//2 = k+1.
        # So connect index-k-th node to index-(k+2)-node.
        slow.next = slow.next.next;
            
        return head;