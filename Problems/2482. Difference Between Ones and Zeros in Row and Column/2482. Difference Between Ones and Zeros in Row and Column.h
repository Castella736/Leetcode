# include <vector>
using namespace std;
class Solution {
public:
    vector<vector<int>> onesMinusZeros(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        int* onesRow = new int[m]();
        int* onesCol = new int[n]();

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                onesRow[i] += grid[i][j];
                onesCol[j] += grid[i][j];
            }
        }

        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                grid[i][j] = (2*onesRow[i]-n) + (2*onesCol[j]-m);

        delete[] onesRow;
        delete[] onesCol;
        return grid;
    }
};