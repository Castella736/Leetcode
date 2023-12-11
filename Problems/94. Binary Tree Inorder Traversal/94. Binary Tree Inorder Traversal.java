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
import java.util.List;
import java.util.ArrayList;
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> record = new ArrayList(); // Record the result.
        if (root == null) return record;

        // Traverse left node.
        record.addAll(inorderTraversal(root.left));
        // Traverse mid node.
        record.add(root.val);
        // Traverse right node.
        record.addAll(inorderTraversal(root.right));
        
        return record;
    }
}