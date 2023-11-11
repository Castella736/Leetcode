# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque;
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([(root, 1)]); # define pending node queue.
        max, res_level = root.val, 1;
        cur_sum, cur_level = 0, 1;
        
        # BFS until all nodes visitied.
        while queue:
            cur, height = queue.popleft();
            
            # This means the previous level sum is over.
            if cur_level < height: 
                # Update if the previous level sum is better.
                if cur_sum > max:
                    max = cur_sum;
                    res_level = cur_level;
                # Advance to the next level record;
                cur_level += 1;
                cur_sum = 0;
            
            # Add sum to the level.
            cur_sum += cur.val;
            
            # Add pending nodes
            if cur.left:
                queue.append((cur.left,height+1));
            if cur.right:
                queue.append((cur.right,height+1));
                
        # Check the last level.
        if cur_sum > max:
            res_level = cur_level;
            
        return res_level;