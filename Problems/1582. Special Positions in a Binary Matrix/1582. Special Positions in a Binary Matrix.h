# include <vector>
using namespace std;
class Solution {
public:
    int numSpecial(vector<vector<int>>& mat) {
        int m = mat.size();
        int n = mat[0].size();
        int res = 0;
        vector<int> colCand;

        // Find column candidate.
        for (auto row: mat) {
            int nOne = 0;
            int pos = -1;
            for (int j = 0; j < n; j ++) {
                if (row[j] == 1) {
                    nOne += 1;
                    pos = j;
                }
            }
            if (nOne == 1) colCand.push_back(pos);
        }

        for (auto col: colCand) {
            int nOne = 0;
            for (int i = 0; i < m; i++)
                nOne += mat[i][col];
            if (nOne == 1) res += 1;
        }

        return res;
    }
};