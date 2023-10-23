# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1==None:
            return list2;
        elif list2==None:
            return list1;

        if list1.val > list2.val:
            return self.mergeTwoLists(list2,list1);

        res = list1;
        now = list1;
        list1 = list1.next;

        while list1!=None and list2!=None:
            if list1.val < list2.val:
                now.next = list1;
                now = list1;
                list1 = list1.next;
            else:
                now.next = list2;
                now = list2;
                list2 = list2.next;
        
        if list1==None:
            now.next = list2;
        else:
            now.next = list1;
        
        return res;