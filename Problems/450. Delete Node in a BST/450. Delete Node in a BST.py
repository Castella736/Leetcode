# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root;
        
        def insert(root: TreeNode, node: Optional[TreeNode]) -> None:
            if node is None:
                return;
            
            cur = root;
            while cur:
                if cur.val > node.val:
                    if cur.left:
                        cur = cur.left;
                    else:
                        cur.left = node;
                        return;
                elif cur.val < node.val:
                    if cur.right:
                        cur = cur.right;
                    else:
                        cur.right = node;
                        return;
            return;
        
        # Search left child.
        if root.val > key:
            if root.left:
                root.left = self.deleteNode(root.left, key);
        # Search right child.
        elif root.val < key:
            if root.right:
                root.right = self.deleteNode(root.right, key);
        # Found the node, start delete an concatenate.
        else:
            # Replace with left child.
            if root.left:
                temp = root.right;
                root = root.left;
                insert(root, temp);
            # Replace with right child.
            elif root.right:
                temp = root.left;
                root = root.right;
                insert(root, temp);
            # Delete leaf
            else:
                root = None;
        
        return root;