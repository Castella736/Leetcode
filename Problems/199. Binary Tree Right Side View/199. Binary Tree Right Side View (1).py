# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Record the result.
        res = [];
        
        # DFS
        def dfs(node: Optional[TreeNode], height: int, res: List[int]) -> None:
            # Exclude empty node.
            if node is None:
                return None;
            
            # Update right most value.
            if len(res) == height:
                res.append(node.val);
                
            # Recur the process.
            dfs(node.right, height+1, res);
            dfs(node.left, height+1, res);
            
            return None;
        
        dfs(node=root, height=0, res=res);
            
        return res;