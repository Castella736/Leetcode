# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # If the node is not a leave, its depth is the maximum of its children + 1.
        if root:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1;
        # If the node is None i.e. child of a leave, its depth is 0.
        else:
            return 0;