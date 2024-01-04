# include <vector>
# include <string>
# include <algorithm>
using namespace std;

class Solution {
public:
    int numberOfBeams(vector<string>& bank) {
        int res = 0;
        int cur_count, prev_count = 0;
        for (const string& row: bank) {
            cur_count = count(row.begin(), row.end(), '1');
            if (cur_count > 0) {
                res += prev_count * cur_count;
                prev_count = cur_count;
            }
        }
        return res;
    }
};