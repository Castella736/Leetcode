# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Use recursion to search BST.
        if root is None: # If end, return None.
            return None;
        
        if root.val == val: # If hit value, return current.
            return root;
        elif root.val > val: # If larger than target, search in left child.
            return self.searchBST(root.left, val);
        else: # If less than targe, search in right child.
            return self.searchBST(root.right, val);