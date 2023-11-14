# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque;
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        p, q = deque([root.left]), deque([root.right]);
        
        while p and q:
            cur_l = p.popleft();
            cur_r = q.popleft();
            
            if not cur_l and not cur_r:
                continue;
            elif not cur_l or not cur_r:
                return False;
            
            if cur_l.val != cur_r.val:
                return False;
            
            p.append(cur_l.left);
            p.append(cur_l.right);
            q.append(cur_r.right);
            q.append(cur_r.left);
            
        return len(p)==len(q);