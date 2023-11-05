# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Use a queue to store pending nodes and its depth.
        # Initialize with the root with depth 1.
        stack = deque([(root,1)]);
        res = 0; # Record the maximum depthm seen.
        
        # DFS
        while stack:
            cur, depth = stack.pop();
            
            if cur:
                if depth>res:
                    res=depth;
                stack.append([cur.right, depth+1]);
                stack.append([cur.left, depth+1]);
        
        return res;