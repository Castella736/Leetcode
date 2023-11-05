# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevNode = None;
        curNode = head;
        while curNode:
            nextNode = curNode.next; # Store next.
            curNode.next = prevNode; # Reverse the link.
            # Advance to the next.
            prevNode = curNode;
            curNode = nextNode;
        
        return prevNode;