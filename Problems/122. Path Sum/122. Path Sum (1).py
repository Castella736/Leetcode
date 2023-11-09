# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Exclude empty root.
        if not root:
            return False;
        
        # If leaf, check if val == targetSum.
        if not (root.left or root.right):
            return targetSum == root.val;
        
        # Recursive check children.
        return (
            self.hasPathSum(root.left, targetSum-root.val)
            or self.hasPathSum(root.right, targetSum-root.val)
        );