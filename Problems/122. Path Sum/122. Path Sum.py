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
        
        stack = [(root, root.val)]; # (node, sum to the node).
        
        # DFS
        while stack:
            cur, cur_sum = stack.pop();
            
            # If leaf, check if the currenct sum is target.
            if not (cur.right or cur.left):
                if cur_sum == targetSum:
                    return True
            
            if cur.right:
                stack.append((cur.right,cur_sum+cur.right.val));
            if cur.left:
                stack.append((cur.left,cur_sum+cur.left.val));
            
        return False;