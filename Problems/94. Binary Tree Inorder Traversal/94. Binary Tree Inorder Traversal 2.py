# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque;
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # List to record result.
        res = [];
        
        # Auxilary inoder recursive function.
        def inorder(node: Optional[TreeNode]) -> None:
            # Terminal condition.
            if node is None:
                return;
            
            # Capture the result list.
            nonlocal res;
            
            # Traversing order.
            inorder(node.left);
            res.append(node.val);
            inorder(node.right);
            
            return;
        
        # Apply auxilary function to the root.
        inorder(root);
        
        return res;