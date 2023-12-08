# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque;
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        # Exclude empty node.
        if root is None:
            return "";
        
        # Preorder search.
        root.val = str(root.val);
        if root.left is None and root.right is None:
            return root.val;
        elif root.right is None:
            return root.val + f"({self.tree2str(root.left)})";
        
        return root.val + f"({self.tree2str(root.left)})" + f"({self.tree2str(root.right)})";
    
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res = deque([]); # list to record result
        
        # Preorder search.
        def preorder(node):
            # Exclude empty node.
            if node is None:
                return;
            
            nonlocal res;
            # Write mid node.
            res.append(str(node.val));
            # Check if the node is leaf.
            if node.left is None and node.right is None:
                return;
            
            # Write left node.
            res.append('(');
            preorder(node.left);
            res.append(')');
            # Write right node if it exists.
            if node.right is not None:
                res.append('(');
                preorder(node.right);
                res.append(')');
                
        # Run preorder search.
        preorder(root);
            
        # Recast the result into string.
        return "".join(res);