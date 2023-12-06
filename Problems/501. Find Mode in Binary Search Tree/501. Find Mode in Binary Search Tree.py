# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        prev = None;
        cur_streak = 0;
        max_streak = 0;
        mode = set();
        
        # Regualr inorder search.
        def inorder(root):
            if root is None:
                return;
            
            nonlocal prev, cur_streak, max_streak;
            
            inorder(root.left);
            
            # Verify if the two nums are consecutive.
            if root.val == prev:
                cur_streak += 1;
            else:
                cur_streak = 1;
                prev = root.val;
            
            # Check if the streak of the value hits max streak.
            if cur_streak == max_streak:
                mode.add(root.val);
            elif cur_streak > max_streak:
                mode.clear();
                max_streak = cur_streak;
                mode.add(root.val);
            
            inorder(root.right);
            
        inorder(root);
        
        return list(mode);