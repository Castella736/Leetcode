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
# include <vector>
using namespace std;
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> record{}; // Record the result.
        if (root == nullptr) return record;

        vector<int> tmp; // Used to store temp result.
        // Traverse left node.
        tmp = inorderTraversal(root->left);
        record.insert(record.end(), tmp.begin(), tmp.end());

        // Traverse mid node.
        record.push_back(root->val);

        // Traverse right node.
        tmp = inorderTraversal(root->right);
        record.insert(record.end(), tmp.begin(), tmp.end());
        
        return record;
    }
};