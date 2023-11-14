# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque;
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0;
        
        queue = deque([(root, 1)]);
        
        while queue:
            cur, height = queue.popleft();
            
            if not cur.left and not cur.right:
                return height;
            
            if cur.left:
                queue.append((cur.left, height+1));
            if cur.right:
                queue.append((cur.right, height+1));