# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque;
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Store all nodes in a array;
        array = deque();
        while head is not None:
            array.append(head);
            head = head.next;
        
        # Exclude list of len 1 or 2.
        if len(array) <= 2:
            return;
        
        # Perform double head queue concatenate.
        while len(array)>1:
            first = array.popleft();
            last = array.pop();
            first.next, last.next = last, first.next;
        # Avoid loop.
        last.next.next = None;
        
        return None;