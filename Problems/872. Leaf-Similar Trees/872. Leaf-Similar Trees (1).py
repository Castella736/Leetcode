# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
        
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def extractLeaf(root: Optional[TreeNode]) -> List[int]:
            """Return the leaf values sequence of a tree starting from left.

            Args:
                root (TreeNode): root of the tree.

            Returns:
                deque(): The sequence of leaf values of the tree.
            """
            if not root: # root is None
                return [];
            
            if not (root.left or root.right): # Root is a leaf
                return [root.val];
                
            # If root is a regular node.
            return extractLeaf(root.left)+(extractLeaf(root.right));
        
        return extractLeaf(root1) == extractLeaf(root2);