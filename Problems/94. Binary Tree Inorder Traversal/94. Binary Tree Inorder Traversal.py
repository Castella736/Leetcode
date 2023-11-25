# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque;
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = [];
        # Use an extra boolean to record if the node visited.
        stack = deque([(root, False)]);
        
        # Perform inorder traverse.
        while stack:
            cur, visited = stack.pop();
            # Terminal of tree nodes
            if not cur:
                continue;
            
            # Check if cur node seen.
            if visited:
                res.append(cur.val);
            else:
                # Add pending nodes
                stack.append((cur.right, False));
                stack.append((cur, True));
                stack.append((cur.left,False));
                
        return res;