/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
#include <string>
#include <sstream>
using namespace std;
class Solution {
private:
    // Preorder traversal to translate node to string.
    void preorder(TreeNode* node, stringstream& ss) {
        // Exclude empty node.
        if (!node) {
            return;
        }

        // Append mid node content.
        ss << std::to_string(node->val);
        if (node->left || node->right) {
            // Append left node content.
            ss << "(";
            preorder(node->left, ss);
            ss << ")";   
        }
        if (node->right) {
            // Append right node content.
            ss << "(";
            preorder(node->right, ss);
            ss << ")";
        }
    }
public:
    string tree2str(TreeNode* root) {
        stringstream ss; // Helper string stream.
        preorder(root, ss); // Run preorder traversal.
        return ss.str(); // Return the result.
    }
};