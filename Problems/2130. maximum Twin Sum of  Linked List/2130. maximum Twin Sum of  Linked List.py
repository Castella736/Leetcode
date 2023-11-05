# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Fast-slow two pointers and reverse half list while traversing.
        # Initializing condition
        slow, fast = head, head.next;
        nextNode = slow.next;
        head.next = None;
        
        while fast.next and fast.next.next:
            # Advance the fast pointer.
            fast = fast.next.next;
            # Advance the slow pointer and reverse the link.
            preNode = slow;
            slow = nextNode;
            nextNode = slow.next;
            slow.next = preNode;
        
        # Start search maximum twin sum from the middle.
        fast = nextNode;
        res = 0;
        while fast:
            res = max(res, fast.val+slow.val);
            fast, slow = fast.next, slow.next;
        
        return res;