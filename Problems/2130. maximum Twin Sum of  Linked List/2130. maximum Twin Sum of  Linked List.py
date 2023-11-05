# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Traverse the list and turn it to array.
        curNode = head;
        record = [];
        while curNode:
            record += [curNode.val];
            curNode = curNode.next;
        
        # Find maximum twin sum in the array
        res = 0;
        n = len(record);
        for i in range(n//2):
            if record[i]+record[n-1-i] > res:
                res = record[i]+record[n-1-i];
            
        return res;