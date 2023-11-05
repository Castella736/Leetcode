# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Exclude None.
        if not head:
            return head;
        
        # Use an extra pre-pointer to reverse the order.
        curNode, nextNode = head, head.next;
        head.next = None;
        
        while nextNode:
            # Advance to the next node.
            preNode = curNode;
            curNode = nextNode;
            nextNode = nextNode.next;
            # Reverse the link of "cur" in this loop.
            curNode.next = preNode;
        
        return curNode;