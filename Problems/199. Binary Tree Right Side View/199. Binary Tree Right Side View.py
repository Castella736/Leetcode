# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque;
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Exclude empty tree.
        if root is None:
            return [];
        
        queue = deque([(root, 0)]); # Queue to record traverse.
        res = []; # Record the result.
        
        # BFS
        while queue:
            cur, height = queue.popleft();
            
            # Update right most value.
            if len(res) == height:
                res.append(cur.val);
                
            # Add pending nodes.
            if cur.right:
                queue.append((cur.right, height+1));
            if cur.left:
                queue.append((cur.left, height+1));
            
        return res;