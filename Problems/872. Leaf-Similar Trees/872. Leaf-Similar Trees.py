# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque;
class Solution:
    def extractLeaf(self, root: Optional[TreeNode]) -> deque():
        """Return the leaf values sequence of a tree starting from left.

        Args:
            root (TreeNode): root of the tree.

        Returns:
            deque(): The sequence of leaf values of the tree.
        """
        # Stack DFS.
        stack = deque([root]); # A stack to record visiting.
        res = deque(); # A list to store result.
        cur = None; # current node pointer.
        
        # Start DFS until all node visited.
        while stack:
            cur = stack.pop();
            # If cur is not a leaf,
            # append children to the stack such that left visited first.
            if cur.right:
                stack.append(cur.right);
            if cur.left:
                stack.append(cur.left);
            # If cur is a leaf,
            # record the value.
            if not (cur.left or cur.right):
                res.append(cur.val);
            
        return res;
            
        
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.extractLeaf(root1) == self.extractLeaf(root2);