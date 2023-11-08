# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque;
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        stack = deque([(root,root.val)]); # Stack to record pending visit.
        res = 1; # Int to store result, init. as 1 since the root is always good.
        
        def appendChildren(node: TreeNode, max_in_path: int) -> None:
            """Append the node the stack.

            Args:
                node (TreeNode): The node whose children are being appended.
                max_in_path (int): Maximum value in the pass path to the node (exclusive).

            Returns:
                None: This function alters global variables "res" and "stack".
            """
            nonlocal res;
            nonlocal stack;
            
            if node.val >= max_in_path:
                stack.append( (node, node.val) );
                res += 1
            else:
                stack.append( (node, max_in_path) );
            return None;
        
        while stack:
            # Load top of the stack to verify its children.
            cur, max_in_path = stack.pop();
            # Append its children if they are not empty.
            # During the appending, check if they are good simultaneously.
            if cur.right:
                appendChildren(cur.right, max_in_path);
            if cur.left:
                appendChildren(cur.left, max_in_path);
            
        return res;