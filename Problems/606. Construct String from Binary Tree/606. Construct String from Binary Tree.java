/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    // Preorder traversal to translate node to str
    private static void preorder(TreeNode node, StringBuilder ss) {
        // Exclude empty node.
        if (node == null) {
            return;
        }

        // Append mid node content.
        ss.append(String.valueOf(node.val));
        if (node.left!=null || node.right!=null) {
            // Append left node content.
            ss.append("(");
            preorder(node.left, ss);
            ss.append(")");
        }
        if (node.right != null) {
            // Append right node content.
            ss.append("(");
            preorder(node.right, ss);
            ss.append(")");
        }
    }

    public String tree2str(TreeNode root) {
        StringBuilder ss = new StringBuilder(); // Helper string stream.
        preorder(root, ss); // Run preorder traversal.
        return ss.toString(); // Return the result.
    }
}